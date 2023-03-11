from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from users.forms import RegisterForm
from django.contrib.auth.views import LoginView

# Create your views here.

class UserRegistration(FormView):
    template_name = 'users/registration.html'
    form_class = RegisterForm
    success_url = reverse_lazy('users:success')

    def form_valid(self, form):
        form.save()
        return super(UserRegistration, self).form_valid(form)
    
class UserLogin(LoginView):
    template_name = 'register/login.html'
    fields = '__all__'
    redirect_autheticated_user = True
    success_url = reverse_lazy('inicio')

    def get_success_url(self):
        return reverse_lazy('inicio')