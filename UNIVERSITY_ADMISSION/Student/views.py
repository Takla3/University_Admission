from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import mixins
from Student.serializers import StudentCertificationMarksSerializer
from Student.models import Certificate
from django_filters.rest_framework import DjangoFilterBackend

from Student.serializers import StartAdmissionSerializer
from Student.models import Admission
# Create your views here.


class StudentCertificationMarksViewSet(
    mixins.RetrieveModelMixin,
    GenericViewSet,
):
    """
    API provides default `retrieve()`, and `list()` actions.

        Permissions: no Authentication required.
    """
    queryset = Certificate.objects.all()
    serializer_class = StudentCertificationMarksSerializer
    lookup_field = 'seat_number'

class StartAdmissionViewSet(
    mixins.CreateModelMixin,
    GenericViewSet,
):
    serializer_class = StartAdmissionSerializer
    queryset = Admission.objects.all()

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
