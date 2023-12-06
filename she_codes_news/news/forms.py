from django import forms
from django.forms import ModelForm
from .models import NewsStory
from django.contrib.auth import get_user_model


class StoryForm(ModelForm):
    class Meta:
        model = NewsStory
        fields = ['title','category', 'image_url', 'pub_date', 'content']
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

    