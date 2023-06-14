# Generated by Django 4.2.1 on 2023-06-10 09:14

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdmissionType',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='CertificateType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Governorate',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Marks',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('mark', models.CharField(max_length=40)),
                ('certificate_type_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admission.certificatetype')),
            ],
        ),
        migrations.CreateModel(
            name='Majors',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('year', models.IntegerField(validators=[django.core.validators.MinValueValidator(2020), django.core.validators.MaxValueValidator(9999)])),
                ('gender', models.BooleanField()),
                ('min_pass_grade', models.DecimalField(decimal_places=2, max_digits=6)),
                ('admission_type_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admission.admissiontype')),
                ('certificate_type_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admission.certificatetype')),
                ('governorate_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admission.governorate')),
            ],
        ),
        migrations.CreateModel(
            name='MajorMark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('min_pass_grade', models.DecimalField(decimal_places=2, max_digits=6)),
                ('major_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mark_major_set', to='Admission.majors')),
                ('mark_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admission.marks')),
            ],
        ),
        migrations.CreateModel(
            name='consideredMarks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('min_pass_grade', models.DecimalField(decimal_places=2, max_digits=6)),
                ('major_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='considered_marks_major_set', to='Admission.majors')),
                ('mark_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admission.marks')),
            ],
        ),
    ]
