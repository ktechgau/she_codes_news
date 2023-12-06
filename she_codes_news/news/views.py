from django.views import generic
from .models import NewsStory,StoryCategory
from django.urls import reverse_lazy
from .forms import StoryForm
from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth.models import User
from django.views.generic import ListView


class IndexView(generic.ListView):
    template_name = 'news/index.html'
    context_object_name = "all_stories"

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.all().order_by('-pub_date')[:4]
        context['CategoryChoices'] = StoryCategory.CategoryChoices.choices

        #context['search_form'] = SearchForm()
        return context
    
class StoryView(generic.DetailView):
    model = NewsStory
    template_name = "news/story.html"
    context_object_name = "story"

class AddStoryView(generic.CreateView):
    form_class = StoryForm
    context_object_name = 'news/createStory.html'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super() .form_valid(form)
    

    

    
#     model = NewsStory
#     template_name = 'news/search_results.html'
#     context_object_name = 'stories'

#     def get_queryset(self):
#         form= SearchForm(self.request.GET)
#         queryset = super().get_queryset()

    #     if form.is_valid():
    #         category = form.cleaned_data('category')
    #         author = form.cleaned_data['author']

    #         if category:
    #             queryset = queryset.filter(category=category)

    #         if author:
    #             queryset = queryset.filter(author=author)
        

    #     return queryset
    
    # def get_context_data(self, **kwargs):
    #     context = supßer().get_context_data(**kwargs)
    #     context['form'] = SearchForm(self.request.GET)
    #     return context
    
    # def search_results(request):
    #     view = SearchResultsView.as_view()
    #     return view(request)
        #filtering using author and category
        # queryset = NewsStory.object.filter(category=category, author=author)

    # else:
    #     queryset = NewsStory.objects.all()

    # context = {
    #     'form': form,
    #     'stories': queryset,
    # }

    # return render(request, 'news/search_results.html', context)
# class SearchResultsView(generic.ListView):
#     model = NewsStory
#     form_class_2 = SearchForm
#     template_name = 'news/search_results.html'
#     context_object_name = 'stories'

#     def get_queryset(self):
#         form = SearchForm(self.request.GET)
#         queryset = super().get_queryset()

#         if form.is_valid():
#             category2 = form.cleaned_data.get('category')
#             author_query = form.cleaned_data.get('author')

#             if category2:
#                 queryset = queryset.filter(category=category2)
#             if author_query:
#                 queryset = queryset.filter(Q(author__username__icontains=author_query | Q(author__first_name__icontains=author_query) | Q(author__last_name__icontains=author_query)))
      
#         return queryset

#trying to add the update feature

class EditStoryView(generic.UpdateView):
    model=NewsStory
    form_class = StoryForm
    context_object_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')
    template_name = "update.html"
    #fields = ['title','pub_date', 'content', 'category']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
