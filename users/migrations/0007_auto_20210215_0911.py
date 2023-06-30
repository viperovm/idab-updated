# Generated by Django 3.1.6 on 2021-02-15 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20210211_1424'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teacher',
            name='is_manager',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='teacher',
            name='link',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
