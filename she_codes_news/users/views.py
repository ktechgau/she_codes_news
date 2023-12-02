from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import generic
from .models import CustomUser, UserProfile
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'

# This creates a user profile for newly created user
    def form_valid(self, form):
        response = super().form_valid(form)
        UserProfile.objects.create(user=self.object)
        return response

#Creates a view to display the user profile - login is required

def  account_view(request):
    #ensures user instance is used, not LazyObject
    user_instance=request.user if request.user.is_authenticated else None
    
    #check if user is authorised before trying to get ot create a profile
    if user_instance:
        user_profile, created= UserProfile.objects.get_or_create(user=user_instance)
        return render(request, 'users/account.html', {'user_profile': user_profile})
    else:
        return redirect('login')
