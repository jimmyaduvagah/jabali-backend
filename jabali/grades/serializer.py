from rest_framework.serializers import ModelSerializer

from .models import GradeClass, GradeSubject, GradeScore

class GradeClassSerializer(ModelSerializer):
    class Meta:
        model = GradeClass
        fields = '__all__'


class GradeScoreSerializer(ModelSerializer):
    class Meta:
        model = GradeScore
        fields = '__all__'


class GradeSubjectSerializer(ModelSerializer):
    class Meta:
        model = GradeSubject
        fields = '__all__'

