from django.shortcuts import redirect
from django.views import View


class TodoView(View):
    all_todos = []

    def post(self, request, *args, **kwargs):
        todo_key = request.POST.get('todo')
        important_key = request.POST.get('important')
        if important_key and todo_key not in self.all_todos:
            self.all_todos.insert(0, todo_key)
        elif not important_key and todo_key not in self.all_todos:
            self.all_todos.append(todo_key)
        return redirect('/')
