from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.views import View
from django.shortcuts import render
from .models import Vacancy


class VacancyView(View):
    def get(self, request, *args, **kwargs):
        vacancies = Vacancy.objects.all()
        return render(request, 'vacancy.html', {'vacancies': vacancies})


class NewVacancyView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'new_vacancy.html')

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_staff:
            description = request.POST['description']
            Vacancy(description=description, author=request.user).save()
            return HttpResponseRedirect('/home')
        else:
            return HttpResponseForbidden()
