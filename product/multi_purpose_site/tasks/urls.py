from . import views
from django.urls import path

urlpatterns = [
    path("", views.default_task_view, name="home"),
    path("create", views.task_create, name="create")
]