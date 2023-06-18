from django.shortcuts import render,redirect

from django.http import HttpResponse

#from todoapp.models import Todo
from todoapp.models import c_todo

def todoList(request):
    
    context = {
        'title' : 'Список задач',
        'todoList' : c_todo.objects.all()
    }
    
    return render(request, "list.html", context)


def addTodo(request):
    
    context = {
        'title' : 'Добавление новой задачи',
    }
    
    if request.method == "POST":
        Todotext = request.POST.get("Todotext", "Пусто")
        newtask = c_todo.objects.create(Todotext = Todotext, Tododone = False)
        return redirect('/todo/list')
    else:
        return render(request, "addtodo.html", context)
    
    
def editTodo(request, id):
    
    item_todo = c_todo.objects.get(Todoid = id)
    
    context = {
        'title' : 'Редактирование задачи',
        'todo' : item_todo,
    }
    
    if request.method == "POST":
        
        Tododone = request.POST.get("Tododone", "off")
        if Tododone == 'on': 
            Tododone = True 
        else: 
            Tododone = False
    
        item_todo.Todotext = request.POST.get("Todotext", "Пусто")
        item_todo.Tododone = Tododone
        item_todo.save()
        
        return redirect('/todo/list')
    else:
        return render(request, "edittodo.html", context)
    
    
def delTodo(request, id):
        
    c_todo.objects.get(Todoid = id).delete()

    return redirect('/todo/list')

    
    
    