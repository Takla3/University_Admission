from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Majors
from .serializers import MajorSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter

# import django_filters

# class ReplacementFilter(django_filters.FilterSet):
#     start_date = DateFilter(
#         field_name='start_date',
#         lookup_expr='gte',
#         widget=DateInput(attrs={'type': 'date'})  # 🖘 specify widget
#     )
#     end_date = DateFilter(
#         field_name='end_date',
#         lookup_expr='lte',
#         widget=DateInput(attrs={'type': 'date'})  # 🖘 specify widget
#     )

#     class Meta:
#         model = Replacement
#         fields = ['start_date', 'end_date']


class MajorList(generics.ListCreateAPIView):
    queryset = Majors.objects.all()
    serializer_class = MajorSerializer
    filter_backends = [
        DjangoFilterBackend,
        OrderingFilter,
    ]
    filterset_fields = [
        'governorate_id__name',
        'governorate_id',
        'min_pass_grade',
    ]
    ordering_fields = [
        'governorate_id__name',
        'governorate_id',
    ]

    def get_queryset(self):
        return super().get_queryset()
