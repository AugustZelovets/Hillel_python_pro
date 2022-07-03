from django.urls import path
from django.views.generic import TemplateView

from .views import *

app_name = 'blog'

urlpatterns = [
    path('', get_all_posts, name='get_all_posts'),
    path('category/<slug:category_slug>/', get_posts_by_category, name='get_posts_by_category'),
    path('post/<slug:post_slug>/', get_one_post, name='get_one_post'),
    path('add_post/', add_post, name='add_post'),
    path('add_category/', add_category, name='add_category'),
    path('user_posts/<str:user>/', get_user_posts, name = 'user_posts'),


]
