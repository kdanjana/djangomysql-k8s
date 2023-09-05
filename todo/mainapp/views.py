from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.list import ListView


from .forms import TodoForm
from .models import Todo

# Create your views here.

class MainPageView(View):
    def get(self, request):
        new_todoform = TodoForm()
        taskslist = Todo.objects.filter(completed=False)
        tasks_list = taskslist.order_by("-created_at")
        context = {
            "form": new_todoform,
            "tasks_list": tasks_list
        }
        return render(request, "mainapp/main.html", context)


    def post(self, request):
        submitted_todoform = TodoForm(request.POST)
        if submitted_todoform.is_valid():
            submitted_todoform.save()
            return redirect("mainapp:main")
        else:
            return render(request, "mainapp/main.html", {"form": submitted_todoform})


def TaskCompleted(request, task_id):
    task = Todo.objects.get(pk=task_id)
    task.completed = True
    task.save()
    return redirect("mainapp:main")


class EditTaskView(View):
    def get(self, request, task_id):
        todo_db = Todo.objects.get(pk=task_id)
        edit_todoform = TodoForm({"task": todo_db.task})
        context = {
            "form": edit_todoform,
            "item_id": task_id
        }
        return render(request, "mainapp/edittask.html", context)

    def post(self, request, task_id):
        edited_todoform = TodoForm(request.POST)
        if edited_todoform.is_valid():
            editted_task = edited_todoform.cleaned_data.get('task')
            task_from_db = Todo.objects.get(pk=task_id)
            task_from_db.task = editted_task
            task_from_db.save()
            return redirect("mainapp:main")
        else:
            return render(request,"mainapp/edittask.html", edited_todoform)


class ListTasksView(ListView):
    model = Todo
    context_object_name = "tasks"
    template_name = "mainapp/listtasks.html"
    def get_queryset(self):
        qs = super().get_queryset()
        data = qs.filter(completed=True)
        return data

def DeleteAllTasks(request):
    Todo.objects.filter(completed=True).delete()
    return redirect("mainapp:main")
