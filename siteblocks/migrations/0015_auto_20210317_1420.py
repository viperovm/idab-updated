# Generated by Django 3.1.6 on 2021-03-17 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteblocks', '0014_remove_subsection_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='excerption',
            field=models.TextField(blank=True, null=True, verbose_name='Цитата'),
        ),
        migrations.AlterField(
            model_name='subsection',
            name='excerption',
            field=models.TextField(blank=True, null=True, verbose_name='Цитата'),
        ),
    ]
