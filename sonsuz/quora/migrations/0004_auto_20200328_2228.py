# Generated by Django 2.2.10 on 2020-03-28 14:28

from django.db import migrations
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('quora', '0003_auto_20200326_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='content',
            field=mdeditor.fields.MDTextField(verbose_name='答案内容'),
        ),
    ]
