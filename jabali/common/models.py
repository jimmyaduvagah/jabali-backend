import uuid

from django.db import models
from django.utils import timezone

GENDER_CHOICES = (
    ('MA', 'Male'),
    ('FM', 'Female')
)


class AbstractBase(models.Model):
    """Base class for all models that belong to a business partner."""

    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    created = models.DateTimeField(db_index=True, default=timezone.now)
    created_by = models.UUIDField(null=True, blank=True)
    updated = models.DateTimeField(db_index=True, default=timezone.now)
    updated_by = models.UUIDField(null=True, blank=True)

    def preserve_created_and_created_by(self):
        """Ensure that created and created_by are not changed during updates."""
        try:
            original = self.__class__.objects.get(pk=self.pk)
            self.created = original.created
            self.created_by = original.created_by
        except self.__class__.DoesNotExist:
            pass

    def save(self, *args, **kwargs):
        """Ensure validations are run and updated/created preserved."""
        self.updated = timezone.now()
        self.full_clean(exclude=None)
        self.preserve_created_and_created_by()
        super(AbstractBase, self).save(*args, **kwargs)

    class Meta:
        """Define a default least recently used ordering."""

        abstract = True
        ordering = ('-updated', '-created')
