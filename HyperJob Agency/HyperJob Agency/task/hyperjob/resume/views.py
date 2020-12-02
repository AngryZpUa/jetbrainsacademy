from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.views import View
from django.shortcuts import render
from .models import Resume


class ResumeView(View):
    def get(self, request, *args, **kwargs):
        resumes = Resume.objects.all()
        return render(request, 'resume.html', {'resumes': resumes})


class NewResumeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'new_resume.html')

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated and not request.user.is_staff:
            description = request.POST['description']
            Resume(description=description, author=request.user).save()
            return HttpResponseRedirect('/home')
        else:
            return HttpResponseForbidden()
