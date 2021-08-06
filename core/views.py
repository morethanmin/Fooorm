from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from .models import User as UserModel, Choices as ChoicesModel, Questions as QuestionsModel, Answer, Form, Responses
import json
import random
import string

def home(request) :
  if not request.user.is_authenticated:
    return HttpResponseRedirect(reverse('login'))
  return HttpResponseRedirect(reverse('forms'))

def login(request) :
  if request.user.is_authenticated:
    return HttpResponseRedirect(reverse('forms'))
  if request.method == "POST":
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(request, username = username, password = password)
    if user is not None:
      auth.login(request, user)
      return HttpResponseRedirect(reverse('home'))
    else:
      return render(request, "login.html", {"message": "아이디 또는 비밀번호가 옳지 않습니다."})
  return render(request, 'login.html')

def logout(request) :
  auth.logout(request)
  return render(request, 'login.html')

def signup(request) :
  if request.user.is_authenticated:
      return HttpResponseRedirect(reverse('forms'))
  if request.method == "POST":
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    passwordConfirm = request.POST['passwordConfirm']
    if len(username) < 5 :
      return render(request, "signup.html", {
          "message": "아이디는 6자 이상이어야합니다.",
    })
    if any(sym in username for sym in '!@#$%^&*'):
      return render(request, "signup.html", {
          "message": "특수문자를 사용할 수 없습니다."
    })
    if len(UserModel.objects.filter(username="username"))==1:
      return render(request, "signup.html", {
          "message": "이미 존재하는 아이디입니다."
    })
    if len(UserModel.objects.filter(email="email"))==1:
      return render(request, "signup.html", {
          "message": "이미 존재하는 이메일입니다."
    })
    if len(password) < 5 :
      return render(request, "signup.html", {
          "message": "비밀번호는 6자 이상이어야합니다.",
          "username": username,
          "email": email,
    })
    if password != passwordConfirm:
      return render(request, "signup.html", {
          "message": "비밀번호가 서로 다릅니다.",
          "username": username,
          "email": email,
    })
    user = UserModel.objects.create_user(username = username, email = email, password = password, )
    user.save()
    auth.login(request, user)
    return HttpResponseRedirect(reverse('home'))
  return render(request, 'signup.html')

def forms(request) :
  if not request.user.is_authenticated:
    return HttpResponseRedirect(reverse('login'))
  forms = Form.objects.filter(creator = request.user)

  
  return render(request, 'forms/index.html',{"forms": forms})

def form(request) :

  return render(request, 'forms/_key/index.html')

def form_add(request) :
  if not request.user.is_authenticated:
    return HttpResponseRedirect(reverse('login'))
  if request.method == "POST":
    data = json.loads(request.body)
    title = data["title"]
    key = ''.join(random.choice(string.ascii_letters + string.digits) for x in range(20))
    choices = ChoicesModel(choice = "Option 1")
    choices.save()
    question = QuestionsModel(question_type = "multiple", question_name= "새로운 질문", required= False)
    question.save()
    question.choices.add(choices)
    question.save()
    form = Form(key = key, title = title, creator=request.user)
    form.save()
    form.questions.add(question)
    form.save()
    return JsonResponse({"message": "Sucess", "key": key})

def form_edit(request,key) :

  return render(request, 'forms/_key/edit.html')

def responses(request) :

  return render(request, 'forms/_key/responses.html')
