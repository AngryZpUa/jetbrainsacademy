from django.views import View
from django.shortcuts import render


class MyIndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')