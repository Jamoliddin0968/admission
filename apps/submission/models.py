from django.db import models
from apps.accounts.models import User
from apps.areas.models import EducationalArea


class GenderChoices(models.TextChoices):
    male = ('M', 'Male')
    female = ('F', 'Female')


class AppStatusChoices(models.TextChoices):
    accepted = ('accepted', 'ACCEPTED')
    checking = ('checking', 'CHECKING')
    rejected = ('rejected', 'REJECTED')


class PassportInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    birthdate = models.DateField()
    gender = models.CharField(max_length=1, choices=GenderChoices.choices)
    country = models.CharField(max_length=64)
    district = models.CharField(max_length=64)
    image = models.ImageField()


class ContactInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    country = models.CharField(max_length=64)
    state = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    street = models.CharField(max_length=64)
    postal_code = models.CharField(max_length=16)


class Application(models.Model):
    faculty = models.ForeignKey(EducationalArea, on_delete=models.CASCADE)
    status = models.CharField(max_length=8, choices=AppStatusChoices.choices)
