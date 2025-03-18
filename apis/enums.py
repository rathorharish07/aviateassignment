from django.db import models
from django.utils.translation import gettext_lazy as _


class GENDER(models.TextChoices):
    MALE = 'MALE', _('Male')
    FEMALE = 'FEMALE', _('Female')
    OTHER = 'OTHER', _('Other')


