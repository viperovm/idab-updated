# Generated by Django 3.1.6 on 2021-06-16 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0017_auto_20210402_1427'),
        ('courses', '0008_auto_20210220_1428'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursesblock',
            name='programs',
            field=models.ManyToManyField(blank=True, related_name='courses_blocks', to='programs.Program', verbose_name='Блоки дсциплин'),
        ),
        migrations.AlterField(
            model_name='course',
            name='blocks',
            field=models.ManyToManyField(blank=True, related_name='courses', to='courses.CoursesBlock', verbose_name='Блоки дсциплин'),
        ),
    ]
