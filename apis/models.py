from django.db import models
from .enums import GENDER
from django.core.validators import RegexValidator
from django.core.validators import MinValueValidator


class Candidate(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(
        validators=[
            MinValueValidator(0)
        ],
    )
    gender = models.CharField(max_length=10, choices=GENDER.choices)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(
        max_length=20,
        validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$')],
        help_text='Enter a valid phone number'
    )

