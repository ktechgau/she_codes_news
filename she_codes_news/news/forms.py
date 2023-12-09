from django import forms
from django.forms import ModelForm
from .models import NewsStory
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
     

#Accessing the category choices from database
    #category = forms.ChoiceField(choices=NewsStory._meta.get_field('category').choices)


#Search feature category
# class SearchForm(forms.Form):
# #     category = forms.ChoiceField(
# #         choices=NewsStory.CategoryChoices.choices, required=False,
# #         widget=forms.Select(attrs={'class': 'form-control'}),)
    
# # Search feature via author  
#     author = forms.ModelChoiceField(
#         queryset=get_user_model().objects.all(), required=False,
#         widget=forms.Select(attrs={'class': 'form-control'}),
#         )

    