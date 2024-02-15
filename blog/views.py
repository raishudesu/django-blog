from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
from django.core.paginator import Paginator

# Create your views here.


def post_list(request):
    posts = Post.published.all()
    paginator = Paginator(posts, 5)
    page_number = request.GET.get("page", 1)
    posts = paginator.page(page_number)
    return render(request, "blog/post/list.html", {"posts": posts})


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
    return render(request, "blog/post/detail.html", {"post": post})
