from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import mixins
from Student.serializers import StudentCertificationMarksSerializer
from Student.models import Certificate
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.parsers import JSONParser
from Student.serializers import PostAdmissionSerializer
from Student.models import Admission, Student
from .serializers import StartAdmissionSerializer, StudentSerializer
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


class PostAdmissionViewSet(
    mixins.CreateModelMixin,
    GenericViewSet,
):
    serializer_class = PostAdmissionSerializer
    queryset = Admission.objects.all()

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class StartAdmissionAPIView(generics.GenericAPIView):
    serializer_class = StartAdmissionSerializer
    # parser_classes = JSONParser

    @action(detail=False)
    def start_admission(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        student_instance = Student.objects.get(
            first_name=serializer.data['first_name'],
            middle_name=serializer.data['middle_name'],
            last_name=serializer.data['last_name'],
            birth_date=serializer.data['birth_date'],
            national_id=serializer.data['national_id'],
        )
        student_instance.email = serializer.data['email']
        student_instance.save()

        Certificate.objects.get(
            total_marks=serializer.data['total_marks'],
            seat_number=serializer.data['seat_number'],
            student_id=student_instance.id,
        )
