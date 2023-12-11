from django.urls import path
from .views import CreateAccountView, account_view, UpdateProfileView, DeleteProfileView
from . import views
app_name = 'users'

urlpatterns = [
    path ('create-account/', CreateAccountView.as_view(), name='createAccount'),
    path('account/', account_view, name='account_view'),
    path('editprofile/<int:pk>', views.UpdateProfileView.as_view(), name='update_profile'),
    path('editprofile/<int:pk>/deleteprofile', views.DeleteProfileView.as_view(), name='delete_profile'),
]