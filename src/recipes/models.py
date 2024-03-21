from django.db import models

# Create your models here.

class Recipe(models.Model):
    name= models.CharField(max_length=200)
    cooking_time= models.IntegerField()
    difficulty= models.CharField(max_length=20)
    ingredients= models.TextField(max_length=1000)

    def __str__(self):
        return str(self.name)