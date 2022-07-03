from django.urls import path, include
import os.path
from .views import *

app_name = 'user'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('sign_up/', signup, name='sign_up')
]
