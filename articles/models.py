from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse


class Article(models.Model):
    title = models.CharField(max_length=300)
    body = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    #The auto_now set the field to now everytime the object is saved...... 
    # best known for "last modified"
    #The auto_now_add set the field to now when the object is created....
    # best known for "current date of creation"
    #Setting the auto_now or auto_now_add=True will cause the field to be editable=False and blank=True
    #The auto_now and auto_now_add option will always use the default timezone 
    # at the moment of creation or update. If you need something different, you may want to consider
    # using your own callable default or overriding save() or Using a DateTimeField instead of a 
    # DateField and deciding how to handle the conversion from datetime to date at display time.
    #Even though the date field by default will not be displayed in the admin site, we can still 
    # get to display it on our site by referencing it in the template used

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article_detail", args=[str(self.id)])
        