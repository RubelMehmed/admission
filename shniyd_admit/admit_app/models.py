# from django import forms
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

#=================>Course Data >=====================#


class Course(models.Model):
    name = models.CharField(max_length=32)
    duration = models.CharField(max_length=22)
    deadline = models.DateTimeField(auto_now_add=True)
    prerequisite = models.CharField(max_length=100)
    Fee = models.IntegerField(null=True)

    def __str__(self):
        return self.name

#================> Applicant data <===================#


class Applicant(models.Model):
    applicant_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
   
    email = models.EmailField()
    father_name = models.CharField(max_length=100)
    father_contact = models.CharField(max_length=100)
    selected_course = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    show = models.BooleanField(default=False)

    def __str__(self):
        return self.name

# =======Admin =====


class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
# ------for custom permissions
