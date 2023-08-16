from django.http import Http404
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import mixins
from Student.serializers import StudentCertificationMarksSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.parsers import JSONParser
from Student.serializers import PostAdmissionSerializer
from Student.models import Admission, Student, RequiredDocuments, AdmissionDesire, Certificate, AdmissionRequirements
from .serializers import AdmissionRequirementsSerializer, DocumentSerializer, StartAdmissionSerializer, StatusDesiresSerializer, StudentSerializer, AdmissionDesireSerializer, StatusAdmissionSerializer
from rest_framework.response import Response
from rest_framework import status, generics
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.parsers import MultiPartParser, FormParser


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
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     return serializer.data['id']

    # def start_admission(self, request, *args, **kwargs):
    #     admission_id = self.create_admission(request, *args, **kwargs)

    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)

    #     total_marks = serializer.data['total_marks']
    #     certificate_type_id = serializer.data['certificate_type_id']

    #     admission_type_id = serializer.data['admission_type_id']


class StartAdmissionViewSet(GenericViewSet):
    serializer_class = StartAdmissionSerializer
    # parser_classes = JSONParser

    def handle_exception(self, exc):
        if isinstance(exc, Http404):
            return Response({"message": str(exc)}, status=status.HTTP_404_NOT_FOUND)
        if isinstance(exc, ObjectDoesNotExist):
            return Response({"message": str(exc)}, status=status.HTTP_404_NOT_FOUND)
        return super().handle_exception(exc)

    @action(methods=['POST'], detail=False)
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

        desire_serializer = AdmissionDesireSerializer(
            data=request.data['admission_desires'], many=True)
        desire_serializer.is_valid(raise_exception=True)
        desire_serializer.save()

        # documents_data.is_valid()
        return Response({"data": "Success"})


class StatusDesiresViewSet(GenericViewSet):
    serializer_class = StatusAdmissionSerializer
    # parser_classes = JSONParser

    def handle_exception(self, exc):
        if isinstance(exc, Http404):
            return Response({"message": str(exc)}, status=status.HTTP_404_NOT_FOUND)
        if isinstance(exc, ObjectDoesNotExist):
            return Response({"message": str(exc)}, status=status.HTTP_404_NOT_FOUND)
        return super().handle_exception(exc)

    @action(methods=['POST'], detail=False)
    def get_status_desires(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        student_obj = Student.objects.get(
            user_id__email=serializer.data['email']
        )
        print(serializer.data)
        admission_obj = Admission.objects.get(
            student_id=student_obj.id,
            admission_num=serializer.data['admission_num'],
        )
        student_admission_id = student_obj.student_admission.all().first().id
        print(student_admission_id)
        admission_desire = AdmissionDesire.objects.filter(
            admission_id=student_admission_id
        )
        dict = {
            'admission_status': admission_obj,
            'admission_desires': admission_desire
        }
        # print(dict)
        admission_desire_serializer = StatusDesiresSerializer(dict)
        # admission_desire_serializer.is_valid()

        print(admission_desire_serializer.data)

        return Response(admission_desire_serializer.data)


class AdmissionRequirementsViewSet(
    mixins.CreateModelMixin,
    GenericViewSet,
):
    serializer_class = AdmissionRequirementsSerializer
    queryset = AdmissionRequirements.objects.all()
    parser_classes = [MultiPartParser, FormParser]
