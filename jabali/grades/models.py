from django.db import models
from jabali.common.models import AbstractBase
from jabali.students.models import Student


class GradeClass(AbstractBase):
    class_name = models.CharField(null=False, unique=True, max_length=100)
    class_grade = models.CharField(null=False, max_length=10)
    description = models.CharField(null=True, blank=True, max_length=255)
    students = models.ForeignKey(Student, null=True, on_delete=models.PROTECT)


class GradeSubject(AbstractBase):
    subject_name = models.CharField(null=False, blank=False, unique=True, max_length=100)
    description = models.CharField(null=True, blank=True, max_length=255)


class GradeScore(AbstractBase):
    subject = models.ForeignKey(GradeSubject, null=False, on_delete=models.PROTECT)
    class_grade = models.ForeignKey(GradeClass, null=False, on_delete=models.PROTECT)
    term = models.CharField(null=True, blank=True, max_length=20)
    year = models.DecimalField(null=False, max_digits=4, decimal_places=0)
    student = models.ForeignKey(Student, null=False, on_delete=models.PROTECT)
