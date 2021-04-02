from rest_framework import viewsets

from rest_framework import viewsets

from grades.serializer import GradeClassSerializer, GradeScoreSerializer, \
    GradeSubjectSerializer, GradeSubject, GradeScore, GradeClass

class GradeClassViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing GradeClass instances.
    """
    serializer_class = GradeClassSerializer
    queryset = GradeClass.objects.all()


class GradeSubjectViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing GradeSubject instances.
    """
    serializer_class = GradeSubjectSerializer
    queryset = GradeSubject.objects.all()


class GradeScoreViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing GradeScore instances.
    """
    serializer_class = GradeScoreSerializer
    queryset = GradeScore.objects.all()
