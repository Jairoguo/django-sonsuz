from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.db import models

# Create your models here.
import uuid


from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models

from sonsuz.notifications.views import notification_handler

User = get_user_model()
# from users.models import User


class News(models.Model):
    """新闻动态类"""
    uuid_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True,
                             on_delete=models.SET_NULL, related_name='publishes',
                             verbose_name='用户')
    title = models.CharField(verbose_name="新闻标题", max_length=100)
    content = models.TextField(verbose_name='新闻内容')
    likers = models.ManyToManyField(User, blank=True, related_name="liked_news",
                                    verbose_name='点赞用户')
    reply = models.BooleanField(default=False, verbose_name='是否为评论')
    parent = models.ForeignKey("self", blank=True, null=True, on_delete=models.CASCADE,
                               related_name='children', verbose_name='父级自关联')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间', db_index=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间', db_index=True)

    class Meta:
        verbose_name = '新闻'
        verbose_name_plural = verbose_name
        ordering = ("-updated_at","-created_at")

    def __str__(self):
        return self.content

    def get_content(self):
        return self.content


    def switch_like(self, user):
        """点赞或者取消点赞"""
        if user in self.likers.all():
            self.likers.remove(user) # 如果user曾经点过赞，那么就在self.likers集合里面，就把user移除
        else:
            self.likers.add(user)  # 如果用户没有点赞，那么就把他添加进来
            # 通知楼主
            notification_handler(user, self.user, 'L', self, id_value=str(self.uuid_id), key='social_update')

    def get_parent(self):
        """返回自关联中的上级记录或者本身"""
        if self.parent:
            return self.parent
        else:
            return self

    def get_children(self):
        """获取当前记录的所有子记录"""
        parent = self.get_parent()
        return parent.children.all().select_related('user')

    def reply_this(self, user, text):
        """
        回复新闻的动态
        :param user: 登录的用户
        :param text: 回复的内容
        :return: None
        """
        parent = self.get_parent()
        News.objects.create(
            user=user,
            content=text,
            reply=True,
            parent=parent
        )
        # 通知楼主
        notification_handler(user, parent.user, 'R', parent, id_value=str(self.uuid_id), key='social_update')

    def likers_count(self):
        """点赞数量"""
        return self.likers.count()

    def get_likers(self):
        """所有点赞用户"""
        return self.likers.all()

    def replies_count(self):
        """评论数量"""
        return self.get_children().count()

    def save(self, *args, **kwargs):
        super(News, self).save(*args, **kwargs)

        if not self.reply:
            channel_layer = get_channel_layer()
            payload = {
                "type": "receive",
                "key": "additional_news",
                "actor_name": self.user.username
            }
            async_to_sync(channel_layer.group_send)('notifications', payload)
