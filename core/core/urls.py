"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.views.generic.base import RedirectView
from django.urls import path,include
from todo.views import TaskCreate,TaskUpdate,TaskDelete
from todo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('django.contrib.auth.urls')),
    path('tasks/',TaskCreate.as_view(),name='task-create'),
    path('tasks/<int:pk>/update/',TaskUpdate.as_view(),name='task-update'),
    path('tasks/<int:pk>/delete',TaskDelete.as_view(), name="task-delete"),
    path('',RedirectView.as_view(url = '/tasks')),
    path('accounts/profile/',RedirectView.as_view(url = '/tasks')),
    path('task/',RedirectView.as_view(url = '/tasks')),
    path("register/", views.sign_up, name="register"),
    path("tasks/api/v1/",include('todo.api.v1.urls')),
    path('api-auth/', include('rest_framework.urls'))
]
