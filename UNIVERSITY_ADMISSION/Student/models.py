from django.db import models
from django.contrib.auth.models import AbstractUser
from Admission.models import Governorate,CertificateType,Marks,AdmissionType,Language,Status,Majors

# Create your models here.
class UserAccount(AbstractUser):
      id =models.AutoField(primary_key=True)
      # password=models.CharField(max_length=25)
      avatar=models.ImageField()
      role =models.BooleanField(default=True)
  
class Student(models.Model) :
      id=models.AutoField(primary_key=True)
      first_name=models.CharField(max_length=30)
      middle_name=models.CharField(max_length=30)
      last_name=models.CharField(max_length=30)
      birth_date=models.DateField(null=False)
      mother_name=models.CharField(max_length=30)
      gender=models.BooleanField()
      national_id=models.IntegerField()
      user_id=models.OneToOneField(
            UserAccount,
            on_delete=models.CASCADE
      )

      
      
class Certificate (models.Model):
      id =models.AutoField(primary_key=True)
      certificate_num =models.IntegerField(null=True)
      seat_number=models.IntegerField(unique=True)
      total_marks=models.IntegerField()
      certificate_type_id=models.ForeignKey(CertificateType,on_delete=models.CASCADE)
      governorate_id=models.ForeignKey(Governorate,on_delete=models.CASCADE)
      student_id=models.ForeignKey(Student, on_delete=models.CASCADE)
    
class CertificationMarks(models.Model):
      id =models.AutoField(primary_key=True)
      score=models.IntegerField()
      certificate_id=models.ForeignKey(
            Certificate, 
            on_delete=models.CASCADE,
            related_name= 'marks_certificate_set',
      )
      mark_id=models.ForeignKey(Marks,on_delete=models.CASCADE)
  
    
class Admission(models.Model) :
      id=models.AutoField(primary_key=True)
      admission_type_id=models.ForeignKey(AdmissionType,on_delete=models.CASCADE)
      certificate_student_id=models.ForeignKey(Certificate,on_delete=models.CASCADE,related_name="certificate_admission")
      student_id=models.ForeignKey(Student, on_delete=models.CASCADE)
      language_id=models.ForeignKey(Language,on_delete=models.CASCADE)
      admission_num=models.IntegerField(null=True)
      status_id=models.ForeignKey(Status, on_delete=models.CASCADE)

class AdmissionDesire(models.Model):
    id=models.AutoField(primary_key=True)
    major_id=models.ForeignKey(Majors,on_delete=models.CASCADE)
    admission_id=models.ForeignKey(Admission,on_delete=models.CASCADE)
    priority=models.IntegerField()
    
class RequiredDocuments(models.Model):
    Id=models.AutoField(primary_key=True)
    Admission_Type_Id=models.ForeignKey(AdmissionType,on_delete=models.CASCADE)
    Document_Id=models.IntegerField()
    Document_Name=models.CharField(max_length=30)

class AdmissionRequirements(models.Model):
    id=models.AutoField(primary_key=True)
    document_id=models.ForeignKey(RequiredDocuments,on_delete=models.CASCADE)
    admission_id=models.ForeignKey(Admission,on_delete=models.CASCADE)
    document=models.ImageField()
    valid=models.BooleanField()
    


    
    
    
    
    
    

    

    

    

    
    
    

    
    