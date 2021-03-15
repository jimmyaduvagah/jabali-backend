from django.db import models
from django.conf import settings
from common.models import AbstractBase, GENDER_CHOICES


class GradeClass(AbstractBase):
    class_name = models.CharField(null=False, unique=True, max_length=100)
    class_grade = models.CharField(null=False, max_length=10)
    description = models.CharField(null=True, blank=True, max_length=255)
    students = models.ForeignKey(Student, null=True)


class GradeSubject(AbstractBase):
    subject_name = models.CharField(null=False, blank=False, unique=True, max_length=100)
    description = models.CharField(null=True, blank=True, max_length=255)


class GradeScore(AbstractBase):
    subject = models.ForeignKey(GradeSubject, null=False)
    class_grade = models.ForeignKey(GradeClass, null=False)
    term = models.CharField(null=True, blank=True)
    year = models.d
    student = models.ForeignKey(Student, null=False)
