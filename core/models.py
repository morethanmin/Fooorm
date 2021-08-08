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
    options = models.ManyToManyField(Options, related_name = "options")

class Answer(models.Model):
    answer = models.CharField(max_length=5000)
    question = models.ForeignKey(Questions, on_delete = models.CASCADE ,related_name = "answer_to")

class Form(models.Model):
    key = models.CharField(max_length=30)
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=10000, blank = True)
    creator = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "creator")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    questions = models.ManyToManyField(Questions, related_name = "questions")

class Responses(models.Model):
    key = models.CharField(max_length=20)
    form = models.ForeignKey(Form, on_delete = models.CASCADE, related_name = "response_to")
    answer = models.ManyToManyField(Answer, related_name = "response")
    name = models.CharField(max_length=20)