from django.shortcuts import redirect
from django.views import View


class TodoView(View):
    all_todos = []

    def post(self, request, *args, **kwargs):
        todos = request.POST.get('todo')
        if todos not in self.all_todos:
            self.all_todos.append(todos)
        return redirect('/')
