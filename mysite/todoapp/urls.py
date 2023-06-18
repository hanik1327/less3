from django.urls import path
from . import views

urlpatterns = [
   path('', views.todoList),
   path('list', views.todoList),
   path('addtodo', views.addTodo),
   path('todoedit/<id>', views.editTodo),
   path('tododel/<id>', views.delTodo),
]
