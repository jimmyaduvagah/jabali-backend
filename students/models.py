from django.db import models
from common.models import AbstractBase, GENDER_CHOICES


class Student(AbstractBase):
    first_name = models.CharField(max_length=255, null=False, blank=False, unique=True)
    other_name = models.CharField(max_length=255, null=False, blank=False, unique=True)
    last_name = models.CharField(max_length=255, null=False, blank=False, unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(null=True, blank=True, choices=GENDER_CHOICES, max_length=2)
    is_active = models.BooleanField(default=True)

