# Generated by Django 2.1.4 on 2019-04-05 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rieltor', '0020_auto_20190405_1203'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photo',
            options={'ordering': ['premises']},
        ),
    ]
