from django.contrib import admin
from . models import Posts
# Register your models here.

admin.site.register(Posts) #registering the Posts Model with the admin page so that the admin can have access to the model for CRUD
