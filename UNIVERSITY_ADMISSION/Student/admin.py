from django.contrib import admin

from Admission.models import MajorMark, consideredMarks,AdmissionType

from .models import *

# Register your models here.
admin.site.register(Majors)
admin.site.register(Marks)
admin.site.register(MajorMark)
admin.site.register(consideredMarks)
admin.site.register(CertificateType)
admin.site.register(Governorate)
admin.site.register(Student)
admin.site.register(CertificationMarks)
admin.site.register(Language)
admin.site.register(AdmissionType)
admin.site.register(Admission)
admin.site.register(Status)
admin.site.register(RequiredDocuments)
