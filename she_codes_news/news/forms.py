from django import forms
from django.forms import ModelForm
from .models import NewsStory


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


#Search feature via category and author
class SearchForm(forms.Form):

    category_choices = [(choice, label) for choice, label in NewsStory.CategoryChoices.choices]
    category = forms.ChoiceField(choices=[('', 'Select category')] + category_choices, required=False)
    author = forms.CharField(max_length=100, required=False)

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        self.fields['category'].choices = [
            (choice, choice)for choice, _ in NewsStory.CategoryChoices.choices
        ]