# Generated by Django 3.1.6 on 2021-02-17 13:19

from django.db import migrations, models
import news.models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20210216_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='image',
            field=models.ImageField(max_length=255, upload_to=news.models.image_directory_path, verbose_name='Иллюстрация'),
        ),
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(max_length=255, upload_to=news.models.image_directory_path, verbose_name='Иллюстрация'),
        ),
    ]
