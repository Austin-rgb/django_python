from django.shortcuts import render, redirect
from django.contrib import messages

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
