from django.shortcuts import render
from django.contrib import auth

def home(request) :

  return render(request, 'forms/index.html')

def login(request) :

  return render(request, 'login.html')

def logout(request) :
  auth.logout(request)
  return render(request, 'login.html')

def signup(request) :

  return render(request, 'signup.html')

def forms(request) :

  return render(request, 'forms/index.html')

def form(request) :

  return render(request, 'forms/_pk/index.html')

def edit(request) :

  return render(request, 'forms/_pk/edit.html')

def responses(request) :

  return render(request, 'forms/_pk/responses.html')
