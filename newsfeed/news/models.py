from django.db import models
from django.utils.timezone import now
from datetime import datetime


# Create your models here.

class News(models.Model):
    name = models.CharField(max_length=64)
    text = models.TextField()
    image= models.URLField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    autor = models.CharField(max_length=24, default="")
    
    like_counter = models.PositiveIntegerField(default=0, editable=False)
    dislike_counter = models.PositiveIntegerField(default=0, editable=False)
    view_counter = models.PositiveIntegerField(default=0, editable=False)
    
    
    def __str__(self) -> str:
        return f"{self.name}"