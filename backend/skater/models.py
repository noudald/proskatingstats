from django.db import models


COUNTRIES = (
    ('NL', 'Netherlands'),
)

GENDERS = (
    ('M', 'Male'),
    ('F', 'Female'),
)


class Skater(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDERS)
    country = models.CharField(max_length=2, choices=COUNTRIES)
    birthday = models.DateField()
