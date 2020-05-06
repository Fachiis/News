from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Article


class ArticleListView(ListView):
    model = Article
    context_object_name = 'article_list'
    template_name='article_list.html'


class ArticleDetailView(DetailView):
    model = Article
    template_name='article_detail.html'
    context_object_name = 'article_detail'


class ArticleUpdateView(UpdateView):
    model = Article
    fields = ('title', 'body',) #this indicate the fields am interested in editing
    template_name = "article_update.html"
    #In the instance the context object name is not given, we will use SMALL LETTER OF THE MODEL TO 
    # reference it, in this case "article". This gives us the access to the data base model


class ArticleDeleteView(DeleteView):
    model = Article
    template_name = "article_delete.html"
    success_url = reverse_lazy('article_list')
    #In the instance the context object name is not given, we will use SMALL LETTER OF THE MODEL TO 
    # reference it, in this case "article". This gives us the access to the data base model





