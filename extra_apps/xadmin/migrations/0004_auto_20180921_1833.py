# Generated by Django 2.0 on 2018-09-21 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('xadmin', '0003_auto_20160715_0100'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookmark',
            old_name='users',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='log',
            old_name='users',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='usersettings',
            old_name='users',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='userwidget',
            old_name='users',
            new_name='user',
        ),
    ]
