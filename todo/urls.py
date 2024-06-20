from django.urls import path
from .views import ToDoListView, todo_form


urlpatterns = [

	path('todo_list/', ToDoListView.as_view(), name="todo_list"),
    path('todo_form/',todo_form,name='todo_form'),
	
]
