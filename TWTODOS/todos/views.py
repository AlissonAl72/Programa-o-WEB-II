from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect

from .models import Todos

# Create your views here.

class TodoListView(ListView):
    model = Todos

class TodoCreateView(CreateView):
    model = Todos
    fields = ["title", "deadline"]
    success_url = reverse_lazy("todo_list")

class TodoUpdateView(UpdateView):
    model = Todos
    fields = ["title", "deadline"]
    success_url = reverse_lazy("todo_list")

class TodoDeleteView(DeleteView):
    model = Todos
    success_url = reverse_lazy("todo_list")

class TodoCompleteView(View):
    def get(self, request, pk):
        todo = get_object_or_404(Todos, pk=pk)
        todo.mark_has_complete()
        return redirect("todo_list")