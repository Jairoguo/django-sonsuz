# Generated by Django 2.2.10 on 2020-03-08 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200308_2051'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='住址'),
        ),
    ]
