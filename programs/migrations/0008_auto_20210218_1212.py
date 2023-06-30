# Generated by Django 3.1.6 on 2021-02-18 12:12

from django.db import migrations, models
import programs.models


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0007_auto_20210218_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='training_plan',
            field=models.FileField(blank=True, null=True, upload_to=programs.models.plan_directory_path, verbose_name='Учебный план файл'),
        ),
    ]
