# Generated by Django 2.1.4 on 2019-03-06 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rieltor', '0002_auto_20190306_1652'),
    ]

    operations = [
        migrations.AddField(
            model_name='premises',
            name='image1',
            field=models.ImageField(null=True, upload_to='premises/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='premises',
            name='image2',
            field=models.ImageField(null=True, upload_to='premises/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='premises',
            name='image3',
            field=models.ImageField(null=True, upload_to='premises/%Y/%m/%d'),
        ),
    ]
