from django.urls import include, path
from Student.views import StudentCertificationMarksViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(
    'student_certificate_details',
    StudentCertificationMarksViewSet,
    basename='student_certificate_details',
)
urlpatterns = [
    path('', include(router.urls)),

]
