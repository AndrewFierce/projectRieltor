# Generated by Django 2.1.4 on 2019-04-04 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rieltor', '0010_auto_20190404_1150'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photo',
            options={'ordering': ['premises'], 'permissions': (('view_task', 'Can see available tasks'), ('change_task_status', 'Can change the status of tasks'), ('close_task', 'Can remove a task by setting its status as closed'))},
        ),
        migrations.AlterModelOptions(
            name='premises',
            options={'ordering': ['types', '-date'], 'permissions': (('view_task', 'Can see available tasks'), ('change_task_status', 'Can change the status of tasks'), ('close_task', 'Can remove a task by setting its status as closed'))},
        ),
    ]
