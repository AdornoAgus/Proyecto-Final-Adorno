from django.urls import path
from users import views
from django.views.generic import TemplateView
from templates.register import *

app_name = 'users'

urlpatterns = [
    path('registration/',views.UserRegistration.as_view(), name='registration'),
    path('success/', TemplateView.as_view(template_name='users/success_registration.html'), name='success'),
    path('login/', views.UserLogin.as_view(template_name='register/login.html'), name='login'),

]

