from django.db import models
from phonenumber_field.modelfields import PhoneNumberField




class Profile(models.Model):

    name = models.CharField('name',max_length=100,null=False)
    email = models.EmailField('email',max_length=100,null=False)
    phone_number = models.CharField(max_length=10)
    sumary = models.TextField('sumary',max_length=500, null=False)
    degree = models.CharField('degree',max_length=200)
    university = models.CharField('university',max_length=100)
    previous_work = models.TextField('previous_work',max_length=1000)
    skills = models.TextField('skills',max_length=1000)

