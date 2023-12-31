# Generated by Django 3.1.6 on 2023-01-23 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteblocks', '0015_auto_20210317_1420'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdmittanceDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Дата набора')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Дата набора',
                'verbose_name_plural': 'Даты набора',
            },
        ),
    ]
