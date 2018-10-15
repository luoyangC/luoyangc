# Generated by Django 2.0 on 2018-10-07 10:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('operation', '0006_auto_20180928_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='Archives',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('status', models.SmallIntegerField(default=1, verbose_name='状态')),
                ('content', mdeditor.fields.MDTextField(null=True, verbose_name='动态内容')),
            ],
            options={
                'verbose_name': '动态',
                'verbose_name_plural': '动态',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('status', models.SmallIntegerField(default=1, verbose_name='状态')),
                ('content', models.TextField(verbose_name='留言信息')),
                ('user', models.ForeignKey(default=999, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '留言',
                'verbose_name_plural': '留言',
            },
        ),
    ]
