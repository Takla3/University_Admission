# Generated by Django 4.2.3 on 2023-07-17 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0002_alter_useraccount_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admission',
            name='certificate_student_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='certificate_admission', to='Student.certificate'),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='certificate_num',
            field=models.IntegerField(null=True),
        ),
    ]
