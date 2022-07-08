from django.urls import path
from django.views.generic import TemplateView

from .views import *

app_name = 'blog'

urlpatterns = [
    path('', GetAllPostsView.as_view(), name='get_all_posts'),
    path('category/<slug:category_slug>/', GetPostsByCategoryView.as_view(), name='get_posts_by_category'),
    path('post/<slug:slug>/', GetPostDetailsView.as_view(), name='get_one_post'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('user_posts/<str:username>/', GetPostsByAuthor.as_view(), name='user_posts'),
    path('post_update/<slug>/', PostUpdateView.as_view(), name='post_update'),

]
