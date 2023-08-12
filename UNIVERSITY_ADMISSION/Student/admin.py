from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(UserAccount)
admin.site.register(Student)
admin.site.register(Certificate)
admin.site.register(CertificationMarks)
admin.site.register(AdmissionDesire)
admin.site.register(Admission)
admin.site.register(RequiredDocuments)
admin.site.register(AdmissionRequirements)