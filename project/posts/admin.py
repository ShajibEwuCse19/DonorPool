from django.contrib import admin
from posts.models import Post, Comment, ReviewRating

admin.site.register([Post, Comment, ReviewRating])
