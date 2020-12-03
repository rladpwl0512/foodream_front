from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Blog(models.Model):
    text = models.TextField()

class TestUserProfile(models.Model):
    class Meta:
        ordering = ['id']
        db_table = 'test_user_profile'

        verbose_name = 'TEST User Profile'
        verbose_name_plural = 'TEST User Profile'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=64, default="")
    phone_number =  models.CharField(max_length=20, default="")
    registration_number = models.CharField(max_length=20, default="")