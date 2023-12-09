from django.urls import path, include
from . import views
from .views import IndexView, StoryView, AddStoryView, UpdateStoryView, DeleteStoryView
from users.views import SearchAuthorView


app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.StoryView.as_view(),name='story'),
    path('add-story/', views.AddStoryView.as_view(), name='newStory'),
    path('author/<str:username>', SearchAuthorView.as_view(), name='author_search'),
    path('edit/<int:pk>', views.UpdateStoryView.as_view(), name='update_story'),
    path('edit/<int:pk>/delete', views.DeleteStoryView.as_view(), name='delete_story'),
    path('users/', include('users.urls')),
]
