from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import ListView

from .forms import TodoForm
from .models import Todo


def index(request):

    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Todo item added successfully")
            return redirect('todo:index')  # Assuming the URL name for the index view is 'index' under the namespace 'todo'
    else:
        form = TodoForm()
    i = Todo.objects.all().values()

    context = {
        "form": form,
        "item_list": i,
        "title": "TODO LIST",
    }
    return render(request, 'todo/index.html')

def todo_form(request):
    if request.method =='POST':
        form = TodoForm(request.POST)
        if form.is_valid ():
            form.save()
            return redirect('todo_list')
        
    form = TodoForm()
    return render(request,'todo/todo_form.html',{'form':form})

class ToDoListView(ListView):
    model = Todo
    template_name = 'todo/todo_list.html'
    context_object_name = 'todo'