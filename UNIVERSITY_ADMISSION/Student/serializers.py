from django.core.mail import send_mail
from rest_framework import serializers
from .models import Student, Certificate, CertificationMarks, Admission
from .models import *
from django.conf import settings


class StudentNameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = (
            'first_name',
            'middle_name',
            'last_name',
        )

# class CertificateSerializer(serializers.ModelSerializer):
#     Total_Mark = serializers.IntegerField(
#         source = 'Certificate_Id.Total_Marks',
#     )
#     student_details = StudentSerializer(source = 'Student_Id')
#     class Meta:
#         model = Certificate
#         fields = (
#             'Total_Mark',
#             )


class CertificationMarksSerializer(serializers.ModelSerializer):
    mark_name = serializers.CharField(
        source='mark_id.mark',
    )

    class Meta:
        model = CertificationMarks
        fields = (
            'mark_name',
            'score',
        )


class StudentCertificationMarksSerializer(serializers.ModelSerializer):
    student = StudentNameSerializer(
        source='student_id',
        read_only=True,
    )
    marks = serializers.SerializerMethodField(
        read_only=True,
    )

    class Meta:
        model = Certificate
        fields = (
            'student',
            'marks',
            'total_marks',
        )

    def get_marks(self, obj):
        serializer = CertificationMarksSerializer(
            obj.marks_certificate_set,
            many=True,
        )
        return serializer.data


class PostAdmissionSerializer(serializers.Serializer):
    total_marks = serializers.IntegerField(write_only=True)
    governorate_id = serializers.IntegerField(write_only=True)
    seat_number = serializers.IntegerField(write_only=True)
    certificate_type_id = serializers.IntegerField(write_only=True)

    admission_type_id = serializers.PrimaryKeyRelatedField(
        queryset=AdmissionType.objects.all())
    language_id = serializers.PrimaryKeyRelatedField(
        queryset=Language.objects.all())

    class Meta:
        model = Admission
        fields = (
            'total_marks',
            'governorate_id',
            'seat_number',
            'certificate_type_id',

            'admission_type_id',
            'language_id',
        )

    def validate(self, attrs):
        print(attrs)
        total_marks = attrs.pop('total_marks')
        governorate_id = attrs.pop('governorate_id')
        seat_number = attrs.pop('seat_number')
        certificate_type_id = attrs.pop('certificate_type_id')

        certificate_obj = Certificate.objects.filter(
            seat_number=seat_number,
            certificate_type_id=certificate_type_id,
            governorate_id=governorate_id,
            total_marks=total_marks,
        ).first()

        if not certificate_obj:
            raise serializers.ValidationError({"message": "invalid data"})

        attrs['certificate_student_id'] = certificate_obj
        attrs['student_id'] = certificate_obj.student_id
        attrs['status_id'] = Status.objects.all().first()
        return super().validate(attrs)

    def create(self, validated_data):
        admission_obj = Admission.objects.create(**validated_data)
        return admission_obj

    def to_representation(self, instance):
        return {'id': instance.id}

# ------------------------------------------------


class StudentSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(source='user_id__email')

    class Meta:
        model = Student
        fields = (
            'id',
            'first_name',
            'middle_name',
            'last_name',
            'birth_date',
            'national_id',
            'email',
            # 'mother_name',
            # 'gender',
        )


class CertificateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Certificate
        fields = (
            'total_marks',
            'seat_number',
            'student_id',
        )


class AdmissionDesireSerializer(serializers.ModelSerializer):
    major_name = serializers.CharField(source="major_id.name")
    governorate_name = serializers.CharField(
        source="major_id.governorate_id.name")

    class Meta:
        model = AdmissionDesire
        fields = (
            'major_id',
            'admission_id',
            'priority',
            'major_name',
            'governorate_name',
        )

    def create(self, validated_data):
        validated_data.pop(governorate_name)
        validated_data.pop(major_name)
        return super().create(validated_data)


class StartAdmissionSerializer(serializers.Serializer):
    # admission_desires = serializers.ListSerializer(
    #     child=AdmissionDesireSerializer(),
    # )
    # Admission desire data
    # major_ids = serializers.ListSerializer()
    # admission_id = serializers.IntegerField()
    # priority = serializers.IntegerField()

    admission_desires = AdmissionDesireSerializer(many=True)
    # Student data
    first_name = serializers.CharField(max_length=30)
    middle_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=30)
    birth_date = serializers.DateField()
    national_id = serializers.IntegerField()
    email = serializers.CharField(max_length=30)

    # Certification data
    seat_number = serializers.IntegerField()
    total_marks = serializers.IntegerField()
    admission_id = serializers.IntegerField()


class DocumentSerializer(serializers.ModelSerializer):

    class Meta:
        model = RequiredDocuments
        fields = (
            'Id',
            'Document_Name',
            'Document_Id',
        )


# ----------------------------------------------------------------


class StatusAdmissionSerializer(serializers.Serializer):
    email = serializers.EmailField()
    admission_num = serializers.IntegerField()
    # desire = serializers.SerializerMethodField(read_only=True)

    # def validate(self, attrs):


class AdmissionStatusSerializer(serializers.ModelSerializer):
    status_name = serializers.CharField(source='status_id.name')

    class Meta:
        model = Admission
        fields = ('status_id', 'status_name')
#    AdmissionDesireSerializer


class StatusDesiresSerializer(serializers.Serializer):
    admission_status = AdmissionStatusSerializer()
    admission_desires = AdmissionDesireSerializer(many=True)

    # -----------------------------------------------------


class AdmissionRequirementsSerializer(serializers.ModelSerializer):
    admission_id = serializers.PrimaryKeyRelatedField(
        queryset=Admission.objects.all())
    document_id = serializers.PrimaryKeyRelatedField(
        queryset=RequiredDocuments.objects.all())
    document = serializers.FileField()

    class Meta:
        model = AdmissionRequirements
        fields = (
            'admission_id',
            'document_id',
            'document',
        )

    def create(self, validated_data):
        admission_requirements_instance = super().create(validated_data)
        admission_instance = validated_data['admission_id']
        admission_instance.admission_num = admission_requirements_instance.id

        # student_id=admission_instance.student_id.user_id.email
        email = admission_instance.student_id.user_id.email
        send_mail(
            'Admission Number',
            f'this is your admission number {admission_instance.id}',
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )

        return admission_requirements_instance
