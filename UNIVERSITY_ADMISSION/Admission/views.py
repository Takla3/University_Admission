from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Majors
from .serializers import MajorSerializer, MinMajorSerializer, RequiredDocumentSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework import filters
import django_filters
from rest_framework.response import Response
from Student.models import RequiredDocuments


class MajorFilter(django_filters.FilterSet):
    min_pass_grade__lte = django_filters.NumberFilter(
        field_name='min_pass_grade', lookup_expr='lte')

    class Meta:
        model = Majors
        fields = ['min_pass_grade__lte',
                  'certificate_type_id',
                  'admission_type_id',
                  'year']


class MajorList(generics.ListAPIView):
    queryset = Majors.objects.all()
    serializer_class = MajorSerializer
    filter_backends = [
        # MajorFilter,
        DjangoFilterBackend,
        OrderingFilter,
    ]
    filterset_fields = [
        'governorate_id__name',
        'governorate_id',
        'min_pass_grade',
        'certificate_type_id',
        'certificate_type_id__type',
        'admission_type_id',
        'admission_type_id__type',
        'year',
    ]
    ordering_fields = [
        'governorate_id__name',
        'governorate_id',
    ]

    def get_queryset(self):
        return super().get_queryset()


class FilteredMajorList(generics.ListAPIView):
    queryset = Majors.objects.all()
    filterset_class = MajorFilter
    filter_backends = [DjangoFilterBackend]

    def list(self, request, *args, **kwargs):
        admission_type_id = self.request.query_params.get(
            'admission_type_id', 1)
        majors = self.filter_queryset(self.get_queryset())
        majors_serializer = MinMajorSerializer(data=majors, many=True)
        majors_serializer.is_valid()

        required_documents = RequiredDocuments.objects.filter(
            Admission_Type_Id=admission_type_id)
        required_document_serializer = RequiredDocumentSerializer(
            data=required_documents, many=True)
        required_document_serializer.is_valid()
        data = {
            'majors': majors_serializer.data,
            'required_documents': required_document_serializer.data,
        }

        return Response(data)
