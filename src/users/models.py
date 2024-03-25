from django.db import models

# Create your models here.

class User(models.Model):
    name= models.CharField(max_length=200)
    email= models.EmailField(default='no email provided')
    # pic = models.ImageField(upload_to='books', default='no_image.jpg')

    def __str__(self):
        return str(self.name)
    