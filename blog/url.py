from django.urls import path

from blog import views

app_name = "blog"
urlpatterns = [
    path("home/", views.blog_home,name="home"),
    path("post/<int:post_id>/", views.blog_post, name="post-view"),
    path("create/", views.blog_create, name="post-write"),
    path("post-edit/<int:post_id>/", views.blog_post_edit, name="post-edit"),
    path("post-delete/<int:post_id>/", views.blog_post_delete, name="post-delete"),
]