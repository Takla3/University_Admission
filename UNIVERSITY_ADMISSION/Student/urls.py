"""
url
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Student.views import StudentCertificationMarksViewSet
from Student.views import PostAdmissionViewSet, StartAdmissionViewSet, StatusDesiresViewSet, AdmissionRequirementsViewSet

router = DefaultRouter()
router.register(
    'student-certificate-details',
    StudentCertificationMarksViewSet,
    basename='student-certificate-details',
)
router.register(
    'post-admission',
    PostAdmissionViewSet,
    basename='post-admission',
)
router.register(
    'upload-required-documents',
    AdmissionRequirementsViewSet,
    basename='upload-required-documents',
)

urlpatterns = [
    path(
        'start-admission/',
        StartAdmissionViewSet.as_view({'post': 'start_admission'}),
        name='start-admission',
    ),
    path(
        'get-status-desires/',
        StatusDesiresViewSet.as_view({'post': 'get_status_desires'}),
        name='get-status-desires',
    ),
    path('', include(router.urls)),
]
