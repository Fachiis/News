""" This module provides the function to create an article and comment object. """
from django.db import models
from django.conf import settings  # for the timezone setting
from django.contrib.auth import get_user_model
from django.urls import reverse


class Article(models.Model):
    """
    An Article class for creating an article.

    Fields:
    title (str): The field column for adding the title of the article.
    body (str): The field column for adding the body of the article.
    author (int): The field column is a foreign linking the user obj to article(s) obj.
    pub_date (d): The field column for adding the date and time creation of article.
    """

    title = models.CharField(max_length=300)
    body = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article_detail", args=[str(self.pk)])


class Comment(models.Model):
    """
    An Comment class for creating a comment obj on an article obj.

    Fields:
    comment (str): The field column for adding the comment.
    author (int): The field column is a foreign linking the user obj to comment(s) obj.
    article (int): The field column is a foreign linking the article obj to comment(s) obj.
    """

    article = models.ForeignKey(
        "Article",
        on_delete=models.CASCADE,
        related_name="comments",
    )
    comment = models.CharField(max_length=150)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse("article_list")
