from rest_framework import viewsets
from teachers.serializer import TeacherSerializer, Teacher

class TeacherViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Teacher instances.
    """
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()
