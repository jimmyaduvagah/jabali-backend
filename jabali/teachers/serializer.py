from rest_framework.serializers import ModelSerializer

from jabali.teachers.models import Teacher


class TeacherSerializer(ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'
