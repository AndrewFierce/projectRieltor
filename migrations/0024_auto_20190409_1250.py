# Generated by Django 2.1.4 on 2019-04-09 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rieltor', '0023_auto_20190405_1350'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='premises',
            options={'ordering': ['types', '-date'], 'permissions': (('can_see_premises', 'Возможность просматривать записи'), ('can_change_premises', 'Возможность редактировать записи'), ('can_delete_premises', 'Возможность удалять записи'), ('can_create_premises', 'Возможность создавать записи'), ('can_change_users', 'Возможность редактировать пользователя'), ('can_delete_users', 'Возможность удалять пользователя'), ('can_create_users', 'Возможность создавать пользователя'), ('can_view_premise1', 'Просмотр 1-ек'), ('can_view_premise2', 'Просмотр 2-ек'), ('can_view_premise3', 'Просмотр 3-ек'), ('can_view_premise4', 'Просмотр 4-ек'), ('can_view_premise_commercial', 'Просмотр коммерческой недвижимости'))},
        ),
    ]
