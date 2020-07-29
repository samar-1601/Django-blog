from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # this is used to get a variable user which has a one-one relation with the user fields i.e for one user only one profile picture can be there in contrary to the blog-posts which can have many-one relation with a user
    # CASCADE means that if we release any user from our database then his profilr is deleted nad not vice-versa
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
