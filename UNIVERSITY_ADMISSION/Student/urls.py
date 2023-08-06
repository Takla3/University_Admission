"""
url
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Student.views import StudentCertificationMarksViewSet
from Student.views import StartAdmissionViewSet

router = DefaultRouter()
router.register(
    'student-certificate-details',
    StudentCertificationMarksViewSet,
    basename='student-certificate-details',
)
router.register(
    'start-admission',
    StartAdmissionViewSet,
    basename='start-admission',
)

urlpatterns = [
    
    path('', include(router.urls)),
    
]
