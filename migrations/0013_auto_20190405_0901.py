# Generated by Django 2.1.4 on 2019-04-05 06:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rieltor', '0012_auto_20190404_1710'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='premises',
            options={'ordering': ['types', '-date'], 'permissions': (('can_see_зremises', 'Возможность просматривать записи'), ('can_see_edit', 'Возможность редактировать записи'))},
        ),
    ]
