from django.db import models

# Create your models here.

class User(models.Model):
    name= models.CharField(max_length=200)
    email= models.EmailField(default='no email provided')

    def __str__(self):
        return str(self.name)
    