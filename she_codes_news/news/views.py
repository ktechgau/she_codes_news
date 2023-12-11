from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.views import generic
from .models import NewsStory,StoryCategory
from django.urls import reverse_lazy
from .forms import StoryForm, CommentForm
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib.auth.models import User
from django.views.generic import ListView, UpdateView, DeleteView


class IndexView(generic.ListView):
    template_name = 'news/index.html'
    context_object_name = "all_stories"

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.all().order_by('-pub_date')[:2]
        context['all_stories'] = NewsStory.objects.all().order_by('-pub_date')[2:]
        
        context['CategoryChoices'] = StoryCategory.CategoryChoices.choices

        #context['search_form'] = SearchForm()
        return context
    
class StoryView(generic.DetailView):
    model = NewsStory
    template_name = "news/story.html"
    context_object_name = "story"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context
    
class AddStoryView(generic.CreateView):
    form_class = StoryForm
    context_object_name = 'news/createStory.html'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super() .form_valid(form)
    

    
class UpdateStoryView(generic.UpdateView):
    model=NewsStory
    template_name = "news/update.html"
    fields = ['title','category', 'image_url', 'pub_date', 'content']
    success_url = reverse_lazy('news:index')
   


class DeleteStoryView(generic.DeleteView):
    model = NewsStory
    template_name = "news/delete.html"
    success_url = reverse_lazy('news:index')
    
  

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

class AddCommentsView(generic.CreateView):
    form_class = CommentForm
    

    def get(self,request, *args, **kwargs):
        return redirect ("news:story", pk=self.kwargs.get("pk"))
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        pk = self.kwargs.get("pk")
        form.instance.story = get_object_or_404 (NewsStory,pk=pk)
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('news:story', kwargs={'pk':self.kwargs.get('pk')})
    




