from . import views
from .views import *
from django.contrib import admin
from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'posts', PostsAPI, basename='posts')



urlpatterns = [
   # path('',PostsAPI.as_view(),name='posts'),
   path('posts/create/', PostsAPI.as_view({'post': 'create'}), name='create_post'),
    path('posts/edit/<int:pk>/', PostsAPI.as_view({'patch': 'update'}), name='edit_post'),
    path('posts/delete/<int:pk>/', PostsAPI.as_view({'delete': 'destroy'}), name='delete_post'),
    path('posts/', PostsAPI.as_view({'get': 'list'}), name='list_posts'),
    path('like/<int:id>/', LikeAPI.as_view({'post': 'create'}), name='like_post'),
    path('comment/<int:id>/', CommentAPI.as_view({'post': 'create'}), name='comment_post'),
    path('savedpost/<int:id>/', SavedPostAPI.as_view({'post': 'create'}), name='saved_post'),
    path('notification/', NotificationAPI.as_view({'post': 'create'}), name='notification'),
    path('message/send/<int:id>', MessageAPI.as_view({'post': 'create'}), name='message'),
    path('message/', MessageAPI.as_view({'get': 'list'}), name='message'),
]
