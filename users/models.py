import uuid

from django.core.validators import validate_email
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .user_manager import UserManager


class User(PermissionsMixin, AbstractBaseUser):
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['first_name', 'last_name', ]
    objects = UserManager()

    # only value in this model that cannot be changed after creation
    # users can change email, preferred names, DB ids, business partners e.t.c
    # unique to user across the whole distributed system
    guid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    phone_number = models.CharField(max_length=32, unique=True)
    id_number = models.CharField(max_length=32, null=True, blank=True, unique=True)


    email = models.EmailField(
        null=True, blank=False, unique=True, validators=[validate_email])
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, blank=False, null=False)
    other_names = models.CharField(max_length=255, null=True, blank=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    created_by = models.ForeignKey(
        'self', on_delete=models.PROTECT, related_name='user_created_by',
        null=True, blank=True)
    updated_by = models.ForeignKey(
        'self', on_delete=models.PROTECT, related_name='user_updated_by',
        null=True, blank=True)
    # holds a user's organization/business_partner identifier UUID
    # the business_partner integer field may be deprecated
    # organisation = models.ForeignKey(
    # BusinessPartner, null=True, blank=True, on_delete=models.PROTECT)

    agreed_to_terms = models.BooleanField(default=False)
    change_pass_at_next_login = models.BooleanField(
        'Change password at next login', default=True)
    last_password_change = models.DateTimeField(null=True, blank=True)
    can_password_expire = models.BooleanField(default=True)

    # Flag to distinguish a regular user from a system user. A system user,
    # e.g. makes requests on behalf of the system
    is_system_user = models.BooleanField(default=False)

    def get_short_name(self):
        return self.short_name

    def get_full_name(self):
        return self.full_name

    @property
    def short_name(self):
        return self.first_name

    @property
    def full_name(self):
        if self.other_names:
            return " ".join(
                [self.first_name, self.other_names, self.last_name])
        return " ".join([self.first_name, self.last_name])

    def has_permissions(self, permissions):
        return set(permissions).intersection(set(self.permission_strings)) == \
            set(permissions)

    @property
    def permission_strings(self):
        field = 'role__role_permissions__permission__name'
        field2 = 'role__role_permissions__permission__children'
        parent = self.user_roles.order_by(field).distinct(field).values_list(
            field, field2
        )
        flat = list(set(parent, []))
        return flat

    @property
    def my_permissions(self):
        return list(
            set([  # coz of same permission on different roles
                rp.permission for role_user in self.user_roles.all()
                for rp in role_user.role.role_permissions.all()
            ])
        )

    @property
    def my_roles(self):
        return [r.role for r in self.user_roles.all()]

    @property
    def my_roles_name(self):
        return self.user_roles.values_list('role__name', flat=True)

    def save(self, *args, **kwargs):
        self.full_clean(exclude=None)
        super(User, self).save(*args, **kwargs)

    def set_password(self, password):
        if self.id is not None and \
                self.password is not None and \
                self.has_usable_password():
            from .user_info import PasswordHistory
            PasswordHistory.objects.create(
                user=self, old_value=self.password,
                organisation=self.organisation,
                created_by=self, updated_by=self)

        super(User, self).set_password(password)

    class Meta:
        ordering = ('first_name', 'last_name', )
