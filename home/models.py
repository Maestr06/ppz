from django.db import models
from django.forms import CharField

# Create your models here.
class Post(models.Model):
    title = CharField(max_length=100)

    
    def __str__(self):
            return self.title
        
