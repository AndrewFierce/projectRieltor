# Generated by Django 2.1.4 on 2019-04-04 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rieltor', '0011_auto_20190404_1608'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photo',
            options={'ordering': ['premises']},
        ),
        migrations.AlterModelOptions(
            name='premises',
            options={'ordering': ['types', '-date']},
        ),
    ]
