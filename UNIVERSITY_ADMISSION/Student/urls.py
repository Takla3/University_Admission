"""
url
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Student.views import StudentCertificationMarksViewSet

router = DefaultRouter()
router.register(
    'student_certificate_details',
    StudentCertificationMarksViewSet,
    basename='student_certificate_details',
)


urlpatterns = [
    
    path('', include(router.urls)),
    
]

print(router.urls)
