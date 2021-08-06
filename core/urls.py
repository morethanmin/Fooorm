from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('siginup/', views.signup, name="signup"),
    path('forms/', views.forms, name="forms"),
    path('forms/<int:pk>', views.form, name="form"),
    path('forms/<int:pk>/edit', views.edit, name="edit"),
    path('forms/<int:pk>/responses', views.responses, name="responses"),
]
