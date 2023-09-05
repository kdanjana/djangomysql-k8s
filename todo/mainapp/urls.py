from django.urls import path

from . import views

app_name = "mainapp"
urlpatterns = [
    path("", views.MainPageView.as_view(), name="main"),
    path("completed/<int:task_id>", views.TaskCompleted, name="taskcomplete"),
    path("listtasks", views.ListTasksView.as_view(), name="listtasks"),
    path("edittask/<int:task_id>", views.EditTaskView.as_view(), name="edittask"),
    path("deleteall", views.DeleteAllTasks,name="deleteall"),
]