from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from Student.serializers import StudentCertificationMarksSerializer
from Student.models import Certificate
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.
class StudentCertificationMarksViewSet(ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = StudentCertificationMarksSerializer
    lookup_field= 'seat_number'
    # filter_backends = [
    #     DjangoFilterBackend,
    # ]
    # filterset_fields = [
    #     'Seat_Number',
    # ]

    # def get_queryset(self):
    #     seat_number = self.request.query_params.get('seat_number') 
    #     return super().get_queryset().filter(Seat_Number=seat_number)