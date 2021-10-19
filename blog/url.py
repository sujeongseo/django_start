from django.urls import path

from blog import views

urlpatterns = [
    path("home/", views.blog_home),
    path("post/", views.blog_post),
    path("creat/", views.blog_create),
]