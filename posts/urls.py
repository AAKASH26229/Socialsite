from django.urls import path, include
from . import views


urlpatterns = [
    path('posts/new/', views.postCreateView, name="new_post"),
    path('', views.postListView, name="posts"),
]
