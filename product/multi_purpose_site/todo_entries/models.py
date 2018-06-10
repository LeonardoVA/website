from django.db import models

class Todo_entries(models.Model):
    """entries model"""
    done = models.BooleanField(default=False)
    description = models.CharField(max_length=50)
