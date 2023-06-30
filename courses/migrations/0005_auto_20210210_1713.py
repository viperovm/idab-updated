# Generated by Django 3.1.6 on 2021-02-10 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20210209_1147'),
        ('courses', '0004_auto_20210210_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='teachers',
            field=models.ManyToManyField(blank=True, null=True, to='users.Teacher', verbose_name='Преподаватели'),
        ),
    ]
