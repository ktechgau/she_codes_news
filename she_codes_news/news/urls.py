from django.urls import path, include
from . import views
from .views import IndexView, StoryView, AddStoryView, EditStoryView
from users.views import SearchAuthorView


app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.StoryView.as_view(),
    name='story'),
    path('add-story/', views.AddStoryView.as_view(), name='newStory'),
    path('author/<str:username>', views.SearchAuthorView.as_view(), name='author_search'),
#trying to do update feature
    path('<int:pk>/edit/', views.EditStoryView.as_view(), name='update_story'),
#an include statement to reference users app
    path('users/', include('users.urls')),
]
