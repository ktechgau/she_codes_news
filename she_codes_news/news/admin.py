from django.contrib import admin
from .models import Comment, StoryCategory, NewsStory

# Register your models here.
admin.site.register(NewsStory)
admin.site.register(StoryCategory)
admin.site.register(Comment)