# Generated by Django 3.1.6 on 2021-02-18 15:28

from django.db import migrations, models
import siteblocks.models


class Migration(migrations.Migration):

    dependencies = [
        ('siteblocks', '0006_auto_20210218_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='avatar',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to=siteblocks.models.rewiever_directory_path, verbose_name='Аватар'),
        ),
    ]
