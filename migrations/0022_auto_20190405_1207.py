# Generated by Django 2.1.4 on 2019-04-05 09:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rieltor', '0021_auto_20190405_1205'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photo',
            options={'ordering': ['premises'], 'permissions': (('can_see_photos', 'Возможность просматривать фотографии'), ('can_change_photos', 'Возможность редактировать фотографии'), ('can_delete_photos', 'Возможность удалять фотографии'), ('can_create_photos', 'Возможность создавать фотографии'))},
        ),
    ]