from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.


def index(request):
    return HttpResponse("Working!")


def post_list(request):
    posts = Post.published.all()
    return render(request, "blog/list.html", {"posts": posts})


def post_detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, "blog/detail.html", {"post": post})
