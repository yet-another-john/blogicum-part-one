from django.shortcuts import render, get_object_or_404
from datetime import datetime
from blog.models import Category, Post


MAIN_PAGE_POSTS = 5


def index(request):
    template = 'blog/index.html'
    post_list = Post.objects.filter(
        is_published=True,
        category__is_published=True,
        pub_date__date__lte=datetime.now()
    ).order_by('title')[:MAIN_PAGE_POSTS]
    context = {'post_list': post_list}
    return render(request, template, context)


def post_detail(request, post_id):
    template = 'blog/detail.html'
    post = get_object_or_404(
        Post.objects.filter(
            is_published=True,
            category__is_published=True,
            pub_date__date__lte=datetime.now()
        ), pk=post_id
    )
    context = {'post': post}
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    category = get_object_or_404(
        Category.objects.filter(
            slug=category_slug,
            is_published=True
        )
    )

    post_list = Post.objects.filter(
        category__slug=category_slug,
        is_published=True,
        pub_date__lte=datetime.now()
    )

    context = {
        'category': category,
        'post_list': post_list
    }
    return render(request, template, context)
