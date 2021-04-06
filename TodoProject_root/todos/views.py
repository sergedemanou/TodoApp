from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import Todo

# Create your views here.
def list_todos_items(request):
    todo_list = Todo.objects.all()
    context = {'todo_list': todo_list}
    return render(request, 'todoApp/list_todos_items.html', context)

def insert_todos_items(request:HttpRequest):
    todo =  Todo(content = request.POST['content'])
    todo.save()
    return redirect('/')

def delete_item(request, pk):
    todo_to_delete = Todo.objects.get(id=pk)
    todo_to_delete.delete()
    return redirect('/')

