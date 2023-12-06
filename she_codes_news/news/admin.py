from django.contrib import admin
from .import models

# Register your models here.
admin.site.register(models.NewsStory)
admin.site.register(models.StoryCategory)