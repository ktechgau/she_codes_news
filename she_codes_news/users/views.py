from typing import Any
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.views import generic
from .models import CustomUser, UserProfile
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from django.shortcuts import render, redirect, get_object_or_404
from news.models import NewsStory
from django.db.models import Q



class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'

# This creates a user profile for newly created user
    def form_valid(self, form):
        response = super().form_valid(form)
        UserProfile.objects.create(user=self.object)
        return response


#creates a view to display the user profile - login required
 
@login_required #ensures login first
def  account_view(request):

    #retrieves users profile or creats one if doesn't exist
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    #Retrieves user stories
    user_stories = NewsStory.objects.filter(author = request.user) 
     
    return render(request, 'users/account.html', {'user_profile':user_profile, 'user_stories': user_stories})
    
class UpdateProfileView(generic.UpdateView):
    model=CustomUser
    template_name="users/update_profile.html"
    fields = ['username', 'email']
    success_url= reverse_lazy('users:account_view')  
    
class DeleteProfileView(generic.DeleteView):
    model = CustomUser
    template_name = "users/delete_profile.html"
    success_url = reverse_lazy('users:account_view')

# Search feature for stories by author
class SearchAuthorView(generic.DetailView):
    model= CustomUser
    template_name = 'news/author_search.html'
    context_object_name = 'author'

    
    def get_object(self, *args, **kwargs):
        return get_object_or_404(CustomUser, username=self.kwargs['username'])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['all_stories'] = NewsStory.objects.filter(author__id=self.object.id)
        return context