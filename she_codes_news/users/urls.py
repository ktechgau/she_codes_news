from django.urls import path
from .views import CreateAccountView, account_view

app_name = 'users'

urlpatterns = [
    path ('create-account/', CreateAccountView.as_view(), name='createAccount'),
    path('account/', account_view, name='account_view'),
]