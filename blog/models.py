from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Posts(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    #date_posted = models.DateTimeField(auto_now=True) takes the current time whenever edited
    #date_posted = models.DateTimeField(auto_now_add=True) takes only the first time when it was created
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #i.e if the user deletes himself from the database, then all his posts will also be deleted

    def __str__(self) :
        return self.title