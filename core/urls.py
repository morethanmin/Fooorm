from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('siginup/', views.signup, name="signup"),
    path('forms/', views.forms, name="forms"),
    path('forms/add', views.form_add, name="form_add"),
    path('forms/<str:key>', views.form, name="form"),
    path('forms/<str:key>/edit', views.form_edit, name="form_edit"),
    path('forms/<str:key>/responses', views.form_responses, name="form_responses"),
]
