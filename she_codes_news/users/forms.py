from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, UserProfile

class CustomUserCreationForm(UserCreationForm):
    bio = forms.CharField(max_length=500, required = True, help_text="Tell us about yourself")
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'bio']



       
