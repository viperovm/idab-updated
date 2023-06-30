# Generated by Django 3.1.6 on 2021-02-10 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckpointsName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Нименование контрольной точки',
                'verbose_name_plural': 'Нименования контрольных точек',
            },
        ),
        migrations.AlterModelOptions(
            name='checkpoint',
            options={'verbose_name': 'Нименование контрольной точки', 'verbose_name_plural': 'Нименования контрольных точек'},
        ),
        migrations.AddField(
            model_name='checkpoint',
            name='description',
            field=models.TextField(default=1, verbose_name='Описание'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='checkpoint',
            name='number',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='checkpoint',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='courses.checkpointsname', verbose_name='Название'),
        ),
    ]
