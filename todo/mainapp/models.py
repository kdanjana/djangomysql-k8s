from django.db import models

# Create your models here.
class Item(models.Model):
    todo = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)
