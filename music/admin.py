from django.contrib import admin

# Register your models here.
from django.contrib import admin
from music.models import Category, Music


admin.site.register(Category)
admin.site.register(Music)