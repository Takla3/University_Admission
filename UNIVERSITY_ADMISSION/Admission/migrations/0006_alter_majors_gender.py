# Generated by Django 4.2.3 on 2023-07-17 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admission', '0005_alter_majors_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='majors',
            name='gender',
            field=models.BooleanField(blank=True, verbose_name=[(True, 'ذكر'), (False, 'أنثى')]),
        ),
    ]
