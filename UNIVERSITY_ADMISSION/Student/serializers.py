from rest_framework import serializers
from .models import Student,Certificate,CertificationMarks

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
    