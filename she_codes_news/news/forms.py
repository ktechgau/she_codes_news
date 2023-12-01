from django import forms
from django.forms import ModelForm
from .models import NewsStory


class StoryForm(ModelForm):
    class Meta:
        model = NewsStory
        fields = ['title','category', 'pub_date', 'content']
        widgets = {
            'pub_date': forms.DateInput (
                format='%m/%d/%Y',
                attrs={
                    'class':'form-control',
                    'placeholder':'Select a date',
                    'type':'date'
                }
            )
        }

#Accessing the category choices from database
    category = forms.ChoiceField(choices=NewsStory._meta.get_field('category').choices)