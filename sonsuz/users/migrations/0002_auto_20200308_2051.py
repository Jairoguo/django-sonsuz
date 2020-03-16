# Generated by Django 2.2.10 on 2020-03-08 12:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': '用户', 'verbose_name_plural': '用户'},
        ),
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, default='', null=True, upload_to='users/avatars/', verbose_name='头像'),
        ),
        migrations.AddField(
            model_name='user',
            name='birthday',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='生日'),
        ),
        migrations.AddField(
            model_name='user',
            name='github',
            field=models.URLField(blank=True, default='', max_length=255, null=True, verbose_name='GitHub链接'),
        ),
        migrations.AddField(
            model_name='user',
            name='introduction',
            field=models.TextField(blank=True, default='用户未填写介绍', null=True, verbose_name='介绍'),
        ),
        migrations.AddField(
            model_name='user',
            name='job',
            field=models.CharField(blank=True, default='用户未填写职业信息', max_length=50, null=True, verbose_name='职业'),
        ),
        migrations.AddField(
            model_name='user',
            name='linkedin',
            field=models.URLField(blank=True, default='', max_length=255, null=True, verbose_name='LinkedIn链接'),
        ),
        migrations.AddField(
            model_name='user',
            name='website_url',
            field=models.URLField(blank=True, default='', max_length=255, null=True, verbose_name='个人网站'),
        ),
        migrations.AddField(
            model_name='user',
            name='weibo',
            field=models.URLField(blank=True, default='', max_length=255, null=True, verbose_name='微博链接'),
        ),
        migrations.AddField(
            model_name='user',
            name='zhihu',
            field=models.URLField(blank=True, default='', max_length=255, null=True, verbose_name='知乎链接'),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='用户名称'),
        ),
    ]