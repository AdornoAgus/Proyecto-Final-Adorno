from django.urls import path
from users import views
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
app_name = 'users'

urlpatterns = [
    path('registration/',views.UserRegistration.as_view(), name='registration'),
    path('success/', TemplateView.as_view(template_name='users/success_registration.html'), name='success'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),

]