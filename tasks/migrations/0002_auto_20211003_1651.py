# Generated by Django 3.1.6 on 2021-10-03 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0033_auto_20210818_1502'),
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='student',
        ),
        migrations.AddField(
            model_name='task',
            name='students',
            field=models.ManyToManyField(related_name='tasks', to='users.Student', verbose_name='Студент'),
        ),
    ]
