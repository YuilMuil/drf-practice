from django.db import models
from django.utils.translation import gettext_lazy as _

from model_utils.fields import AutoCreatedField, AutoLastModifiedField


class DefaultModel(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False, unique=True)
    created_at = AutoCreatedField(_('created_at'))
    updated_at = AutoLastModifiedField(_('updated_at'))

    class Meta:
        abstract = True
