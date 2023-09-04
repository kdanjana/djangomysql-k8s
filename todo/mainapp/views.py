from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.views.generic.list import ListView
# Create your views here.

from .forms import TodoForm
from .models import Item


class MainPageView(View):
    def get(self, request):
        new_todoform = TodoForm()
        itemslist = Item.objects.filter(completed=False)
        items_list = itemslist.order_by("-created_at")
        context = {
            "form": new_todoform,
            "items_list": items_list
        }
        return render(request, "mainapp/main.html", context)


    def post(self, request):
        submitted_todoform = TodoForm(request.POST)
        if submitted_todoform.is_valid():
            #print(submitted_todoform.cleaned_data["todo"])
            #print(submitted_todoform.cleaned_data.get("todo"))
            submitted_todoform.save()
            return redirect("mainapp:main")
        else:
            return render(request, "mainapp/main.html", {"form": submitted_todoform})


def DeleteTask(request, item_id):
    item = Item.objects.get(pk=item_id)
    item.completed = True
    item.save()
    return redirect("mainapp:main")


class EditTaskView(View):
    def get(self, request, item_id):
        item = Item.objects.get(pk=item_id)
        edit_todoform = TodoForm({"todo": item.todo})
        context = {
            "form": edit_todoform,
            "item_id": item_id
        }
        return render(request, "mainapp/edittask.html", context)

    def post(self, request, item_id):
        edited_todoform = TodoForm(request.POST)
        if edited_todoform.is_valid():
            new_todo = edited_todoform.cleaned_data.get('todo')
            task = Item.objects.get(pk=item_id)
            task.todo = new_todo
            task.save()
            return redirect("mainapp:main")
        else:
            return render(request,"mainapp/edittask.html", edited_todoform)


class ListTasksView(ListView):
    model = Item
    context_object_name = "tasks"
    template_name = "mainapp/listtasks.html"
    def get_queryset(self):
        qs = super().get_queryset()
        data = qs.filter(completed=True)
        return data

def DeleteAll(request):
    Item.objects.filter(completed=True).delete()
    return redirect("mainapp:main")
