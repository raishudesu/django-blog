from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post

# Create your views here.


def index(request):
    return HttpResponse("Working!")


def post_list(request):
    posts = Post.objects.all()
    return render(request, "blog/list.html", {"posts": posts})


def post_detail(request, year, month, day, post):
    # post = Post.objects.get(id=id)

    post = get_object_or_404(
        Post,
        status=Post.Status.PUBLISHED,
        slug=post,
        publish__year=year,
        publish__month=month,
        publish__day=day,
    )
    return render(request, "blog/detail.html", {"post": post})
