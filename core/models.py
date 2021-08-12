from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser, models.Model):
    email = models.EmailField(unique = True)

class Options(models.Model):
    name = models.CharField(max_length=5000)
    is_answer = models.BooleanField(default=False)

class Questions(models.Model):
    name = models.CharField(max_length= 10000)
    type = models.CharField(max_length=20)
    required = models.BooleanField(default= False)
    key = models.CharField(max_length = 5000, blank = True)
    options = models.ManyToManyField(Options)

class Answer(models.Model):
    answer = models.CharField(max_length=5000)
    question = models.ForeignKey(Questions, on_delete = models.CASCADE)

class Form(models.Model):
    key = models.CharField(max_length=30)
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=10000, blank = True)
    creator = models.ForeignKey(User, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    questions = models.ManyToManyField(Questions)

class Responses(models.Model):
    key = models.CharField(max_length=20)
    form = models.ForeignKey(Form, on_delete = models.CASCADE)
    answer = models.ManyToManyField(Answer)
    name = models.CharField(max_length=20)