from django import forms
from django.forms import ModelForm
from .models import NewsStory, Comment
from django.contrib.auth import get_user_model


class StoryForm(ModelForm):
    class Meta:
        model = NewsStory
        fields = ['title','category', 'image_url', 'pub_date', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter a title for your story'}),
            'category': forms.Select(attrs={'class': 'form-control', 'placeholder':'Select a category'}),
            'image_url': forms.URLInput(attrs={'class': 'form-control','placeholder':'Enter a URL for your image'}),
            'pub_date': forms.DateTimeInput (format='%d/%m/%Y %H:%M',attrs={'class':'form-control','placeholder':'Select a date','type':'datetime-local' }),
            'content': forms.Textarea(attrs={'class': 'form-control','placeholder': 'Tell your story'}),
        }
     

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['name','body']
        
    
