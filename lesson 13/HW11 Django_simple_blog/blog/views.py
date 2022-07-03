from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView

from .forms import *


def get_all_posts(request):
    all_posts = Post.objects.all()
    categories = Category.objects.all()
    context = {
        'all_posts': all_posts,
        'categories': categories,
        'title': 'Blog homepage'
    }
    return render(request, 'blog/get_all_posts.html', context)


def get_posts_by_category(request, category_slug):
    posts = Post.objects.filter(category__slug=category_slug)
    categories = Category.objects.all()
    current_category = Category.objects.filter(slug=category_slug).get().name
    context = {
        'posts': posts,
        'categories': categories,
        'current_category': current_category,
        'title': current_category

    }
    return render(request, 'blog/get_posts_by_category.html', context)


def get_one_post(request, post_slug):
    categories = Category.objects.all()
    current_post_title = Post.objects.filter(slug=post_slug).get().title
    context = {
        'post': get_object_or_404(Post, slug=post_slug),
        'categories': categories,
        'title': current_post_title

    }
    return render(request, 'blog/get_one_post.html', context)


def get_user_posts(request, user):
    categories = Category.objects.all()

    posts = Post.objects.filter(author__username=user)
    context = {
        'posts': posts,
        'categories': categories,
        'title': user,
        'user': user
    }
    return render(request, 'blog/user_posts.html', context)


@login_required
def add_post(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            new_category = form.save(commit=False)
            new_category.author = request.user
            new_category.save()
            form.save_m2m()
            return redirect('blog:get_all_posts')
        return render(request, 'blog/add_post.html', {'form': form, 'title': 'Add new post'})
    form = AddPostForm()
    return render(request, 'blog/add_post.html', {'form': form, 'title': 'Add new post'})


@staff_member_required
def add_category(request):
    if request.method == 'POST':
        form = AddCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:get_all_posts')
        return render(request, 'blog/add_category.html', {'form': form, 'title': 'Add new category'})
    form = AddCategoryForm()
    return render(request, 'blog/add_category.html', {'form': form, 'title': 'Add new category'})

class A(DetailView):
    pass