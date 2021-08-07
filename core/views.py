from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from .models import User as UserModel, Options as OptionsModel, Questions as QuestionsModel, Answer as AnswerModel, Form as FormModel, Responses as ResponsesModel
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
  return HttpResponseRedirect(reverse('home'))


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
    if len(UserModel.objects.filter(username=username))==1:
      return render(request, "signup.html", {
          "message": "이미 존재하는 아이디입니다."
    })
    if len(UserModel.objects.filter(email=email))==1:
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
  forms = FormModel.objects.filter(creator = request.user).order_by('-created_at')
  return render(request, 'forms/index.html',{"forms": forms})

def form(request,key) :
  form = FormModel.objects.filter(key = key)
  return render(request, 'forms/_key/index.html',{"form": form[0]})

def form_edit(request,key) :
  if not request.user.is_authenticated:
    return HttpResponseRedirect(reverse('login'))
  form = FormModel.objects.filter(key = key)

  return render(request, 'forms/_key/edit.html',{"menu": "edit", "form": form[0]})


def form_success(request,key) :

  return render(request, 'forms/_key/success.html')

def form_responses_summary(request ,key) :
  if not request.user.is_authenticated:
    return HttpResponseRedirect(reverse('login'))
  form = FormModel.objects.filter(key = key)

  return render(request, 'forms/_key/responses/summary.html', {"menu": "responses", "form": form[0]})


def api_login(request) :
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


def api_signup(request) :
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
    if len(UserModel.objects.filter(username=username))==1:
      return render(request, "signup.html", {
          "message": "이미 존재하는 아이디입니다."
    })
    if len(UserModel.objects.filter(email=email))==1:
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

def api_form(request) :
  if not request.user.is_authenticated:
    return HttpResponseRedirect(reverse('login'))
  if request.method == "POST":
    data = json.loads(request.body)
    name = data["name"]
    title = data["title"]
    key = ''.join(random.choice(string.ascii_letters + string.digits) for x in range(20))
    options = OptionsModel(name = "새로운 옵션")
    options.save()
    question = QuestionsModel(name= "새로운 질문", type = "checkbox", required= False)
    question.save()
    question.options.add(options)
    question.save()
    form = FormModel(key = key, name = name, title = title, creator=request.user)
    form.save()
    form.questions.add(question)
    form.save()
    return JsonResponse({"message": "Sucess", "key": key})
  if request.method == "PUT":
    data = json.loads(request.body)
    form = FormModel.objects.filter(key = data["key"])
    if form.count() == 0:
      return HttpResponseRedirect(reverse('404'))
    else: form = form[0]
    if data["name"] == "name":
      form.name = data["value"]
    if data["name"] == "title":
      form.title = data["value"]
    if data["name"] == "description":
      form.description = data["value"]
    form.save()
    return JsonResponse({'message': "success"})
  if request.method == "DELETE":
    data = json.loads(request.body)
    form = FormModel.objects.filter(key = data["form_key"])
    if form.count() == 0:
      return HttpResponseRedirect(reverse('404'))
    else: form = form[0]
    form.delete()
    return JsonResponse({'message': "success"})

def api_form_id(request, key) :
  form = FormModel.objects.filter(key = key)
  if form.count() == 0:
    return HttpResponseRedirect(reverse('404'))
  else: form = form[0]
  if request.method == "POST":
    res_key = ''.join(random.choice(string.ascii_letters + string.digits) for x in range(20))
    response = ResponsesModel(key = res_key, form = form)
    response.save()
    for i in request.POST:
      if i == "csrfmiddlewaretoken":
        continue
      question = form.questions.get(id = i)
      for j in request.POST.getlist(i):
        answer = AnswerModel(answer=j, question = question)
        answer.save()
        response.answer.add(answer)
        response.save()
  return HttpResponseRedirect(reverse('form_success', kwargs={'key': key}))

def api_question(request) :
  if not request.user.is_authenticated:
    return HttpResponseRedirect(reverse('login'))
  if request.method == "POST":
    data = json.loads(request.body)
    options = OptionsModel(name = "새로운 옵션")
    options.save()
    question = QuestionsModel(name= "새로운 질문", type = "checkbox", required= False)
    question.save()
    question.options.add(options)
    question.save()
    form = FormModel.objects.filter(key = data["form_key"])
    if form.count() == 0:
      return HttpResponseRedirect(reverse('404'))
    else: form = form[0]
    form.questions.add(question)
    form.save()
    return JsonResponse({"message": "Sucess"})


def api_question_id(request,id) :
  if not request.user.is_authenticated:
    return HttpResponseRedirect(reverse('login'))
  if request.method == "PUT":
    data = json.loads(request.body)

    question = QuestionsModel.objects.filter(id = id)
    if question.count() == 0:
      return HttpResponseRedirect(reverse("404"))
    else: question = question[0]
    if data["name"] == "name":
      question.name = data["value"]
    if data["name"] == "required":
      question.required = not question.required
    if data["name"] == "type":
      question.type = data["value"]
    question.save()
    return JsonResponse({'message': "success"})
  
  if request.method == "DELETE":
    question = QuestionsModel.objects.filter(id = id)
    if question.count() == 0:
      return HttpResponseRedirect(reverse('404'))
    else: question = question[0]
    question.delete()
    return JsonResponse({'message': "success"})

def api_option(request) :
  if request.method == "POST":
    data = json.loads(request.body)
    option = OptionsModel(name = data["name"])
    option.save()
    question = QuestionsModel.objects.filter(id = data["id"])
    if question.count() == 0:
      return HttpResponseRedirect(reverse('404'))
    else: question = question[0]
    question.options.add(option)
    question.save()
    return JsonResponse({'message': "success"})

def api_option_id(request, id) :

  if request.method == "PUT":
    data = json.loads(request.body)

    option = OptionsModel.objects.filter(id = id)
    if option.count() == 0:
      return HttpResponseRedirect(reverse("404"))
    else: option = option[0]
    if data["name"] == "name":
      option.name = data["value"]
    option.save()
    return JsonResponse({'message': "success"})

  if request.method == "DELETE":
    option = OptionsModel.objects.filter(id = id)
    if option.count() == 0:
      return HttpResponseRedirect(reverse('404'))
    else: question = option[0]
    question.delete()
    return JsonResponse({'message': "success"})

