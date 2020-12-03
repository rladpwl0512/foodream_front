from django.db import models

# Create your models here.

class Mileage(models.Model):
    photo = models.ImageField(upload_to = 'images/', blank = True, null = True)
    title = models.CharField(max_length = 200, null = True)
    group = models.CharField(max_length=200, null = True)
    total_money = models.CharField(max_length= 200, null = True)
    contents = models.TextField(null = True)
    

    def __str__(self):
        return str(self.title)

class Photo(models.Model):
    mileage = models.ForeignKey(Mileage, on_delete = models.CASCADE , null = True, related_name= 'mileage2')
    photo = models.ImageField(upload_to='images/', blank = True, null = True)
    