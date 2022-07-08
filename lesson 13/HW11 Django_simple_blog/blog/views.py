from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, ListView, CreateView

from .forms import *
from .utils import StaffMixin


def get_all_posts(request):
    all_posts = Post.objects.all()
    categories = Category.objects.all()
    context = {
        'posts': all_posts,
        'categories': categories,
        'title': 'Blog homepage'
    }
    print(request.user)
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


def get_user_posts(request, username):
    categories = Category.objects.all()

    posts = Post.objects.filter(author__username=username)
    context = {
        'posts': posts,
        'categories': categories,
        'title': username,
        'username': username,
        'user': request.user
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


def get_one_post(request, post_slug):
    categories = Category.objects.all()
    current_post_title = Post.objects.filter(slug=post_slug).get().title
    context = {
        'post': get_object_or_404(Post, slug=post_slug),
        'categories': categories,
        'title': current_post_title

    }
    return render(request, 'blog/get_one_post.html', context)


class PostUpdateView(UpdateView):
    model = Post
    form_class = AddPostForm
    template_name = 'blog/post_update_form.html'

    def get_success_url(self):
        return reverse('blog:get_all_posts')


class GetAllPostsView(ListView):
    template_name = 'blog/get_all_posts.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['title'] = 'Blog homepage'
        # print(self.kwargs['request'] )
        return context


class GetPostsByCategoryView(ListView):
    template_name = 'blog/get_posts_by_category.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs['category_slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['current_category'] = Category.objects.filter(slug=self.kwargs['category_slug']).get().name
        context['title'] = context['current_category']
        return context


class GetPostsByAuthor(ListView):
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(author__username=self.kwargs['username'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['username'] = self.kwargs['username']
        context['title'] = self.kwargs['username']
        return context


class GetPostDetailsView(DetailView):
    template_name = 'blog/get_one_post.html'
    context_object_name = 'post'

    def get_queryset(self):
        return Post.objects.filter(slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Post.objects.filter(slug=self.kwargs['slug']).get().title
        context['categories'] = Category.objects.all()
        return context


class AddPostView(LoginRequiredMixin, CreateView):
    template_name = 'blog/add_post.html'
    form_class = AddPostForm
    success_url = reverse_lazy('blog:get_all_posts')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Add new post'
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class AddCategoryView(StaffMixin, CreateView):
    template_name = 'blog/add_category.html'
    form_class = AddCategoryForm
    success_url = reverse_lazy('blog:get_all_posts')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Add new category'
        return context

