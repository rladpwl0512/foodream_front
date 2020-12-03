from django.contrib import admin
from .models import Form, Photo

class PhotoInline(admin.TabularInline):
    model = Photo

class PostAdmin(admin.ModelAdmin):
    inlines= [PhotoInline, ]


# Register your models here.
admin.site.register(Form)