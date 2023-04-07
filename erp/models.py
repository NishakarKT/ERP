from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    roll = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)