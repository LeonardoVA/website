from pathlib import Path
from django.shortcuts import render
from django.http import HttpResponse
from .models import Tasks


def default_task_view(request):
    """default view for request"""
    tasks = Tasks.objects.all()
    return render(request, "task.html", {'tasks': tasks})

def task_create(request):
    """View for creating a task"""

