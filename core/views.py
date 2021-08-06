from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from .models import User as UserModel, Choices, Questions, Answer, Form, Responses

def home(request) :
  print()
  if not request.user.is_authenticated:
    return HttpResponseRedirect(reverse('login'))
  forms = Form.objects.filter(creator = request.user)
  return render(request, "forms/index.html", {"forms": forms})

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

  return render(request, 'forms/index.html')

def form(request) :

  return render(request, 'forms/_pk/index.html')

def edit(request) :

  return render(request, 'forms/_pk/edit.html')

def responses(request) :

  return render(request, 'forms/_pk/responses.html')
