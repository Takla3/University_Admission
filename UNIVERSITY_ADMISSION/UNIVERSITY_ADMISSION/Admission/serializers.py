from rest_framework import serializers

from .models import Majors,MajorMark,consideredMarks,Governorate,AdmissionType,Language,CertificateType,Marks,Status,MinValueValidator,MaxValueValidator

class MajorMarkSerializer(serializers.ModelSerializer):
    mark_name = serializers.CharField(
        source = 'mark_id.mark',
    )
    class Meta:
        model = Majors
        fields = (
            'mark_name',
            'min_pass_grade',
            )

class ConsideredMarksSerializer(serializers.ModelSerializer):
    mark_name = serializers.CharField(
        source = 'mark_id.mark',
    )
    class Meta:
        model = Majors
        fields = (
            'mark_name',
            'min_pass_grade',

            ) 
          
class MajorSerializer(serializers.ModelSerializer):

    major = serializers.SerializerMethodField(
        read_only=True ,
    )
    considered_marks = serializers.SerializerMethodField(
        read_only=True ,
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
       
            )

    def get_major(self, obj):
        serializer = MajorMarkSerializer(
            obj.mark_major_set,
            many= True,
        )
        return serializer.data
    
    def get_considered_marks(self, obj):
        serializer = ConsideredMarksSerializer(
            obj.considered_marks_major_set,
            many= True,
        )
        return serializer.data