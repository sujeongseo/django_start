from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect

from blog.models import Post

def blog_home(request):
    post_list = Post.objects.all()
    context ={
        "post_list": post_list,
    }
    return render(request, "blog/index.html", context)


def blog_post(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {
        "post": post
    }
    return render(request, "blog/post.html", context)

def blog_post_edit(request, post_id):
    target_post = Post.objects.get(id=post_id)
    if request.method == "GET":
        context = {
           "post": target_post
        }
        return render(request, "blog/edit.html", context)
    elif request.method == "POST":
        target_post.title = request.POST["title"]
        target_post.content =request.POST["content"]
        target_post.save()
        return HttpResponseRedirect(f"/blog/post/{post_id}/")

def blog_create(request):
    if request.method == "POST":
        new_post = Post()
        new_post.title = request.POST["title"]
        new_post.content = request.POST["content"]
        new_post.likes = 0
        new_post.save()
        return HttpResponseRedirect("/blog/home/")

    return render(request, "blog/create.html")

def blog_post_delete(request, post_id):
    target_post = Post.objects.get(id=post_id)
    if request.method == "GET":
        target_post = Post.objects.get(id=post_id)
        context = {
            "post": target_post
        }
        return render(request, "blog/delete.html", context)
    elif request.method == "POST":
        target_post.delete()
        return HttpResponseRedirect("/blog/home/")