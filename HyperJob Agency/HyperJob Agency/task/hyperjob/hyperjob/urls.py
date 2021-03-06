"""hyperjob URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView
from menu.views import MyIndexView, MySignUpView, MyLoginView, MyProfileView
from resume.views import ResumeView, NewResumeView
from vacancy.views import VacancyView, NewVacancyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MyIndexView.as_view(), name='root_dir'),
    path('resumes', ResumeView.as_view()),
    path('vacancies', VacancyView.as_view()),
    path('login/', RedirectView.as_view(url='/login')),
    path('signup/', RedirectView.as_view(url='/signup')),
    path('signup', MySignUpView.as_view()),
    path('login', MyLoginView.as_view()),
    path('main_menu/', RedirectView.as_view(url='')),
    path('home', MyProfileView.as_view(), name='home'),
    path('resume/new', NewResumeView.as_view()),
    path('vacancy/new', NewVacancyView.as_view()),
]
