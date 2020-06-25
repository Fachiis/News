from django.contrib.auth.mixins import LoginRequiredMixin 
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied #to be used by the dispatch method

from .models import Article


#If a view is using this LoginRequiredMixin, all requests 
# by non-authenticated users will be redirected to the login page(using the login_url)
class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = "article_create.html"
    fields = (
        'title',
        'body',
    )
    login_url = 'login'

    #This is method is what we called authorizaton. Here we are scanning those that are registered or not
    # If registered, set the present logged in user to author if he clicks to create a new article
    # If not registered or not logged in, the form(icon) for creatring a new article will not appear at the nav
    def form_valid(self, form):
        #This code reads that the author field should be linked to the current logged in users.
        form.instance.author = self.request.user
        return super().form_valid(form)


class ArticleListView(LoginRequiredMixin, ListView):
    model = Article
    context_object_name = 'article_list'
    template_name='article_list.html'
    login_url = 'login'


class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Article
    template_name='article_detail.html'
    context_object_name = 'article_detail'
    login_url = 'login'


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    fields = (
        'title', 
        'body',
        ) #this indicate the fields am interested in editing
    template_name = "article_update.html"
    login_url = 'login'
    #In the instance the context object name is not given, we will use SMALL LETTER OF THE MODEL TO 
    # reference it, in this case "article". This gives us the access to the data base model

    #This method is used to check if the 
    # author of the article is indeed the same user who is currently logged-in and trying to make an update
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
    


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    template_name = "article_delete.html"
    success_url = reverse_lazy('article_list')
    login_url = 'login'
    #In the instance the context object name is not given, we will use SMALL LETTER OF THE MODEL TO 
    # reference it, in this case "article". This gives us the access to the data base model

    #This method is used to check if the 
    # author of the article is indeed the same user who is currently logged-in and trying to make a delete
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

    





