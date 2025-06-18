from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render

from django.views.generic import CreateView
from django.urls import reverse_lazy

from users.forms import AppUserCreationForm

# Create your views here.

UserModel = get_user_model()


class AppUserRegisterView(CreateView):
    model = UserModel
    form_class = AppUserCreationForm
    template_name = 'users/registration/register.html'
    success_url = reverse_lazy('login')


class AppUserLoginView(LoginView):
    template_name = 'users/login.html'
    authentication_form = AuthenticationForm
    redirect_authenticated_user = True


class AppUserLogoutView(LogoutView):
    next_page = reverse_lazy('login')


def home(request):
    return render(request, 'home.html')

def create_post(request):
    return render(request, 'create_post.html')


def trip_journal(request):
    return render(request, 'trip_journal.html')



