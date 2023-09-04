from django.urls import path

from . import views

app_name = "mainapp"
urlpatterns = [
    path("", views.MainPageView.as_view(), name="main"),
    path("delete/<int:item_id>", views.DeleteTask, name="deletetask"),
    path("listtasks", views.ListTasksView.as_view(), name="listtasks"),
    path("edittask/<int:item_id>", views.EditTaskView.as_view(), name="edittask"),
    path("deleteall", views.DeleteAll,name="deleteall"),
]