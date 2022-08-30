from django.urls import path
from posts.views import post_view, comment_view, review_view

urlpatterns = [
    # posts
    path('posts/', post_view.PostCreateAndListView.as_view(), name='posts'),
    path('posts/<pk>/detail/', post_view.PostDetailview.as_view(), name='posts-detail'),
    # comments 
    path('comments/<pk>/add', comment_view.CommentCreateView.as_view(), name='comments-add'),
    path('reviews', review_view.ReviewRatingCreateAndListView.as_view(), name='reviews'),
    path('profiles/', post_view.ProfileListView.as_view(), name='profiles'),
]