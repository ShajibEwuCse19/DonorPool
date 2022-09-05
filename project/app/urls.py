from django import views
from django.contrib import admin
from django.urls import URLPattern, path
from . import views as user_views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("", user_views.home, name="home"),
    path("signup/", user_views.signup, name="signup"),  # signup
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="app/login.html"),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(template_name="app/logout.html"),
        name="logout",
    ),
    path("profile/", user_views.profile_view, name="profile"),
    path('delete/<str:id>',user_views.delete_profile,name='delete_profile'),
    path('query/',user_views.query, name='query'),
    path('appointment/',user_views.App,name='Appointment'),
]
