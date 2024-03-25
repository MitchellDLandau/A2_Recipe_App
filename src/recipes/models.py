from django.db import models
from django.shortcuts import reverse

# Create your models here.

class Recipe(models.Model):
    name= models.CharField(max_length=200)
    cooking_time= models.IntegerField()
    difficulty= models.CharField(max_length=20)
    ingredients= models.TextField(max_length=1000)
    pic = models.ImageField(upload_to='recipe', default='no_image.jpg')

    def __str__(self):
        return str(self.name)
    
    def get_absolute_url(self):
       return reverse ('recipes:detail', kwargs={'pk': self.pk})