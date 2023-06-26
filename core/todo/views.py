from django.contrib.auth import login
from django.contrib import messages
from typing import Any, Dict
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .models import Task
from django.views.generic import (
    ListView,
    DetailView,
    FormView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .forms import TaskForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RegisterForm

# Create your views here.


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    success_url = "/task/"
    template_name = "todo/index.html"
    context_object_name = "task"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context["task"] = self.model.objects.all()
        return context


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ["title", "done"]
    template_name = "todo/update.html"
    success_url = "/task/"


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = "/task/"
    template_name = "todo/update.html"

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


def sign_up(request):
    if request.method == "GET":
        form = RegisterForm()
        return render(request, "registration/register.html", {"form": form})
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, "You have singed up successfully.")
            login(request, user)
            return redirect("/task")
        else:
            return render(request, "registration/register.html", {"form": form})
