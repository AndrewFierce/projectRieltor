# Generated by Django 2.1.4 on 2019-04-04 07:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rieltor', '0007_premises_creater'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='premises',
            name='creater',
        ),
    ]