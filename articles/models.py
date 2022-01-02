from django.db import models
from django.conf import settings  # for the timezone setting
from django.contrib.auth import get_user_model
from django.urls import reverse


class Article(models.Model):
    title = models.CharField(max_length=300)
    body = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article_detail", args=[str(self.pk)])


class Comment(models.Model):
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
