""" This module provides the business logic for the article. """
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied

from .models import Article


class ArticleCreateView(LoginRequiredMixin, CreateView):
    """
    An Article View class for creating a new article object.
    """

    model = Article
    template_name = "article_create.html"
    fields = (
        "title",
        "body",
    )
    login_url = "login"

    def form_valid(self, form):
        """Save the current logged in user to the instance of the form author field."""
        form.instance.author = self.request.user
        return super().form_valid(form)


class ArticleListView(LoginRequiredMixin, ListView):
    """
    An Article View class for listing all available articles obj.
    """

    model = Article
    context_object_name = "article_list"
    template_name = "article_list.html"
    login_url = "login"


class ArticleDetailView(LoginRequiredMixin, DetailView):
    """
    An Article View class for listing an article obj.
    """

    model = Article
    template_name = "article_detail.html"
    context_object_name = "article_detail"
    login_url = "login"


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    """
    An Article View class for updating the title and body of an article obj.
    """

    model = Article
    fields = (
        "title",
        "body",
    )
    template_name = "article_update.html"
    login_url = "login"

    def dispatch(self, request, *args, **kwargs):
        """
        Prevent performing the update function if the user obj is not the author of the article obj.
        """
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    """
    An Article View class for deleting an article obj.
    """

    model = Article
    template_name = "article_delete.html"
    success_url = reverse_lazy("article_list")
    login_url = "login"

    def dispatch(self, request, *args, **kwargs):
        """
        Prevent performing the delete function if the user obj is not the author of the article obj.
        """
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
