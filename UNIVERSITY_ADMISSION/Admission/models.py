
from django.db import models
from enum import Enum, unique
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.


@unique
class Gender(Enum):
    ذكر = True
    أنثى = False

    def __str__(self):
        return 'ذكر' if self.value else 'أنثى'


GENDER_CHOICES = [
    (True, 'ذكر'),
    (False, 'أنثى'),
]


class Governorate(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)

    # def __str__(self):
    #     return self.name


class CertificateType(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=40)

    # def __str__(self):
    #     return self.type


class Marks(models.Model):
    id = models.AutoField(primary_key=True)
    mark = models.CharField(max_length=40)
    certificate_type_id = models.ForeignKey(
        CertificateType,
        on_delete=models.CASCADE,
    )

    # def __str__(self):
    #     return f"{self.mark} {self.certificate_type_id}"


class AdmissionType(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=30)

    # def __str__(self):
    #     return self.type


class Majors(models.Model):
    id = models.IntegerField(primary_key=True)
    certificate_type_id = models.ForeignKey(
        CertificateType,
        on_delete=models.CASCADE,
    )
    governorate_id = models.ForeignKey(
        Governorate,
        on_delete=models.CASCADE,

    )
    admission_type_id = models.ForeignKey(
        AdmissionType,
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=50)
    year = models.IntegerField(
        validators=[MinValueValidator(2020), MaxValueValidator(9999)]
    )
    gender = models.BooleanField(
        [(gender.value, str(gender)) for gender in Gender],
        # choices=GENDER_CHOICES,
        blank=True
    )
    min_pass_grade = models.DecimalField(
        max_digits=6,
        decimal_places=2
    )

    # def __str__(self):
    #     return self.name


class MajorMark(models.Model):
    mark_id = models.ForeignKey(
        Marks,
        on_delete=models.CASCADE,
    )
    major_id = models.ForeignKey(
        Majors,
        on_delete=models.CASCADE,
        related_name='mark_major_set',
    )
    min_pass_grade = models.DecimalField(
        max_digits=6,
        decimal_places=2,
    )

    # def __str__(self):
    #     return f"{self.mark_id.mark} {self.major_id.name}"


class consideredMarks(models.Model):
    mark_id = models.ForeignKey(
        Marks,
        on_delete=models.CASCADE,
    )
    major_id = models.ForeignKey(
        Majors,
        on_delete=models.CASCADE,
        related_name='considered_marks_major_set',
    )
    min_pass_grade = models.DecimalField(
        max_digits=6,
        decimal_places=2,
    )


class Language(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)

    # def __str__(self):
    #     return self.name


class Status(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)

    # def __str__(self):
    #     return self.name
