from django.db import models
from django.utils.timezone import now


# Create your models here.

class News(models.Model):
    name = models.CharField(max_length=64)
    text = models.TextField()
    image= models.URLField()
    upload_time = models.DateTimeField()
    
    def __str__(self) -> str:
        return f"{self.name}"