from rest_framework import viewsets
from jabali.students.serializer import StudentSerializer, Student


class StudentViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Student instances.
    """
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
