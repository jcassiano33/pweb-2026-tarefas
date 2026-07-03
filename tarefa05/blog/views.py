from django.shortcuts import render, get_object_or_404
from . models import Post

def index(request):
    context = {
        "posts": Post.objects.all(),
    }
    return render(request, "blog/index.html", context)

def posts(request, id_post):
    context = {
        "post": get_object_or_404(Post, id=id_post)
    }
    return render(request, "blog/post.html", context)