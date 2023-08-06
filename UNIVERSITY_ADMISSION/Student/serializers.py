from rest_framework import serializers
from .models import Student,Certificate,CertificationMarks,Admission
from .models import *

class StudentSerializer(serializers.ModelSerializer):

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
        source = 'mark_id.mark',
    )
    class Meta:
        model = CertificationMarks
        fields = (
            'mark_name',
            'score',
            )

class StudentCertificationMarksSerializer(serializers.ModelSerializer):
    student = StudentSerializer(
        source = 'student_id',
        read_only = True,
    )
    marks = serializers.SerializerMethodField(
        read_only = True,
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
            many= True,
        )
        return serializer.data
    
    
class StartAdmissionSerializer(serializers.Serializer):
    total_marks=serializers.IntegerField(write_only=True)
    governorate_id=serializers.IntegerField(write_only=True)
    seat_number=serializers.IntegerField(write_only=True)
    certificate_type_id=serializers.IntegerField(write_only=True)

    admission_type_id=serializers.PrimaryKeyRelatedField(queryset=AdmissionType.objects.all())
    language_id=serializers.PrimaryKeyRelatedField(queryset=Language.objects.all())

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
        total_marks=attrs.pop('total_marks')
        governorate_id=attrs.pop('governorate_id')
        seat_number=attrs.pop('seat_number')
        certificate_type_id=attrs.pop('certificate_type_id')
        
        certificate_obj = Certificate.objects.filter(
            seat_number=seat_number,
            certificate_type_id=certificate_type_id,
            governorate_id=governorate_id,
            total_marks=total_marks,
        ).first()
        
        if not certificate_obj:
            raise serializers.ValidationError({"message":"invalid data"})

        attrs['certificate_student_id']=certificate_obj
        attrs['student_id']=certificate_obj.student_id
        attrs['status_id']=Status.objects.all().first()
        return super().validate(attrs)

    def create(self, validated_data):
        admission_obj = Admission.objects.create(**validated_data)
        return admission_obj
    
    def to_representation(self, instance):
        return {'message':'success'}
