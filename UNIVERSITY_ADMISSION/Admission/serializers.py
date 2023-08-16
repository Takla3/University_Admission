""" Serializers """

from rest_framework import serializers

from Student.models import AdmissionDesire, Student
from Student.models import Certificate

from .models import (
    GENDER_CHOICES,
    Majors,
    Gender,
    MajorMark,
    consideredMarks,
    Governorate,
    AdmissionType,
    Language,
    CertificateType,
    Marks,
    Status,
    MinValueValidator,
    MaxValueValidator,

)
from Student.models import RequiredDocuments


# get the name of the governorate from Governorate class to use it in major list
class GovernorateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Governorate
        fields = (
            'id',
            'name',
        )


# get the type of the certificate from CertificateType class to use it in major list
class CertificateTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = CertificateType
        fields = '__all__'
# get the marks of each  major and the minimum pass grade


class AdmissionTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = AdmissionType
        fields = '__all__'


class MajorMarkSerializer(serializers.ModelSerializer):
    mark_name = serializers.CharField(
        source='mark_id.mark',
    )

    class Meta:
        model = Majors
        fields = (
            'mark_name',
            'min_pass_grade',
        )


# get one mark for each major and  the minimum pass grade
class ConsideredMarksSerializer(serializers.ModelSerializer):
    mark_name = serializers.CharField(
        source='mark_id.mark',
    )

    class Meta:
        model = Majors
        fields = (
            'mark_name',
            'min_pass_grade',

        )


# list the info about each major
class MajorSerializer(serializers.ModelSerializer):
    """ MajorSerializer """
    major = serializers.SerializerMethodField(
        read_only=True,
    )
    considered_marks = serializers.SerializerMethodField(
        read_only=True,
    )
    gender = serializers.SerializerMethodField()
    # gender = serializers.ChoiceField(choices=GENDER_CHOICES)

    governorate = GovernorateSerializer(
        read_only=True,
        source='governorate_id',
    )
    certificate_type = CertificateTypeSerializer(
        read_only=True,
        source='certificate_type_id',
    )
    admission_type = CertificateTypeSerializer(
        read_only=True,
        source='admission_type_id',
    )

    class Meta:
        model = Majors
        fields = (
            'id',
            'name',
            'min_pass_grade',
            'gender',
            'year',
            'major',
            'considered_marks',
            'certificate_type',
            'governorate',
            'admission_type',

        )

    def get_major(self, obj):
        serializer = MajorMarkSerializer(
            obj.mark_major_set,
            many=True,
        )
        return serializer.data

    def get_considered_marks(self, obj):
        serializer = ConsideredMarksSerializer(
            obj.considered_marks_major_set,
            many=True,
        )
        return serializer.data

    def get_gender(self, obj):
        return str(Gender(obj.gender))
        # return GENDER_CHOICES.get(obj.gender)


class MinMajorSerializer(serializers.ModelSerializer):
    governorate_name = serializers.CharField(
        source="governorate_id.name",
        read_only=True
    )

    class Meta:
        model = Majors
        fields = (
            'id',
            'name',
            'governorate_id',
            'governorate_name',
        )


class RequiredDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequiredDocuments
        fields = (
            'Document_Id',
            'Document_Name',
        )
