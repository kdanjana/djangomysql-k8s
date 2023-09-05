from django.db import models

# Create your models here.
class Todo(models.Model):
    task = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)
