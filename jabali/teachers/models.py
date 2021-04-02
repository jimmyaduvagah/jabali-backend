from django.db import models
from django.conf import settings
from common.models import AbstractBase, GENDER_CHOICES



class Teacher(AbstractBase):
    tutor = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    teacher_number = models.CharField(null=True, blank=True, unique=True, max_length=20)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(null=True, blank=True, choices=GENDER_CHOICES, max_length=2)
