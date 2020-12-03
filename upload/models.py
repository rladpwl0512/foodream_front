from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from social.models import TestUserProfile

# Create your models here.
class Form(models.Model):
    title = models.CharField(max_length =200)
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to ='images/', blank = True, null =True)
    explain = models.TextField()
    deal_method= models.CharField(max_length=200)
    deadline = models.ImageField(upload_to='images',null = True)
    price = models.CharField(max_length=200)
    location = models.CharField(max_length=200)

class Photo(models.Model):
    form = models.ForeignKey(Form, on_delete= models.CASCADE, null = True, related_name='form2')
    photo = models.ImageField(upload_to='images/', blank = True, null = True )
    def delete(self, *args, **kwargs):
        storage, path = self.photo.storage, self.photo.path
        super(Photo, self).delete(*args, **kwargs)
        storage.delete(path)
    

class Deadline(models.Model):
    form = models.ForeignKey(Form, on_delete=models.CASCADE, null = True, related_name ='form3')
    deadline= models.ImageField(upload_to='images/',null= True )
