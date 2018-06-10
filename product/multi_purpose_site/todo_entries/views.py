from pathlib import Path
from django.shortcuts import render
from django.http import HttpResponse
from .models import Todo_entries


# Create your views here.

def defaultView(request):
    """default view for request"""
    todos = Todo_entries.objects.all()
    return render(request, "todo.html", {'todos': todos})
