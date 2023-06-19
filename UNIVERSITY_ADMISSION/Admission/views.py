from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Majors
from .serializers import MajorSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter

class MajorList(generics.ListCreateAPIView):
    queryset = Majors.objects.all()
    serializer_class = MajorSerializer
    filter_backends = [
        DjangoFilterBackend,
        OrderingFilter,
    ]
    filterset_fields = [
        'governorate_id__name',
        'min_pass_grade',
    ]
    ordering_fields = [
        'governorate_id__name',
    ]
    
    def get_queryset(self):
        return super().get_queryset()
        