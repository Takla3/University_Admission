"""
url
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Student.views import StudentCertificationMarksViewSet
from Student.views import PostAdmissionViewSet, StartAdmissionAPIView

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

urlpatterns = [
    path(
        'start-admission/',
        StartAdmissionAPIView.as_view(),
        name='start-admission',
    ),
    path('', include(router.urls)),
]
