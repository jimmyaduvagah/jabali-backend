import uuid
import logging

from django.conf import settings
from django.core.mail import send_mail
from django.core.validators import validate_email
from django.contrib.auth import password_validation
from django.contrib.auth.models import BaseUserManager
from django.template.loader import get_template
from django.utils import timezone




class UserManager(BaseUserManager):

    def create_user(self, email, first_name, last_name,
                    password=None, **extra_fields):
        now = timezone.now()
        if not email:
            raise ValueError('The email must be set')

        email = UserManager.normalize_email(email)
        is_staff = extra_fields.pop('is_staff', False)
        is_active = extra_fields.pop('is_active', True)
        is_superuser = extra_fields.pop('is_superuser', False)
        last_login = extra_fields.pop('last_login', now)
        date_joined = extra_fields.pop('date_joined', now)
        other_names = extra_fields.pop('other_names', None)
        last_password_change = extra_fields.pop('last_password_change', now)

        validate_email(email)
        user = self.model(
            email=email, first_name=first_name,
            last_name=last_name, other_names=other_names,
            is_staff=is_staff, is_active=is_active, is_superuser=is_superuser,
            last_login=last_login, date_joined=date_joined,
            last_password_change=last_password_change, **extra_fields)
        password_validation.validate_password(password, user)
        user.set_password(password)
        if extra_fields.get('guid', None) is None:
            user.guid = uuid.uuid4()

        user.save(using=self._db)

        return user

    def create_superuser(self, email, first_name, last_name,
                         password, **extra_fields):
        user = self.create_user(email, first_name, last_name,
                                password, **extra_fields)
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
