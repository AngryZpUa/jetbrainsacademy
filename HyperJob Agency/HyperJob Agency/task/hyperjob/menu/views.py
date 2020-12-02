from django.contrib.auth.views import LoginView
from django.views import View
from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class MyIndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class MySignUpView(CreateView):
    form_class = UserCreationForm
    success_url = '/login'
    template_name = 'signup.html'


class MyLoginView(LoginView):
    authentication_form = AuthenticationForm
    template_name = 'login.html'
    redirect_authenticated_user = True


class MyProfileView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'profile.html')
