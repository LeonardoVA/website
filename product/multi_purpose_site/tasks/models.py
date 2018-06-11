from django.db import models

class Tasks(models.Model):
    """entries model"""
    done = models.BooleanField(default=False)
    description = models.CharField(max_length=50)
