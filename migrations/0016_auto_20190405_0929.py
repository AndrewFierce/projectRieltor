# Generated by Django 2.1.4 on 2019-04-05 06:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rieltor', '0015_auto_20190405_0925'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='premises',
            options={'ordering': ['types', '-date']},
        ),
    ]
