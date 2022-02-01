from django.urls import path
from .views import home, todo_list

urlpatterns = [
    path("", home, name="home"),
    path("list", todo_list, name="list"),
    path("list", todo_add, name="add"),
]
