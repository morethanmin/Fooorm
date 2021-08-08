from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('siginup/', views.signup, name="signup"),
    path('forms/', views.forms, name="forms"),
    path('forms/<str:key>/', views.form, name="form"),
    path('forms/<str:key>/success', views.form_success, name="form_success"),
    path('forms/<str:key>/edit', views.form_edit, name="form_edit"),
    path('forms/<str:key>/responses/summary', views.form_responses_summary, name="form_responses_summary"),
    path('forms/<str:key>/responses/question', views.form_responses_question, name="form_responses_question"),
    path('forms/<str:key>/responses/response', views.form_responses_response, name="form_responses_response"),

    path('api/login', views.api_login, name="api_login"),
    path('api/signup', views.api_signup, name="api_signup"),
    path('api/form', views.api_form, name="api_form"),
    path('api/form/<str:key>', views.api_form_id, name="api_form_id"),
    path('api/question', views.api_question, name="api_question"),
    path('api/question/<str:id>', views.api_question_id, name="api_question_id"),
    path('api/option', views.api_option, name="api_option"),
    path('api/option/<str:id>', views.api_option_id, name="api_option_id"),
]
