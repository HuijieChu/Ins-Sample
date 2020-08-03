from django.urls import path
from Insta.views import (HelloWorld, PostView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, addLike)
urlpatterns = [
path('', HelloWorld.as_view(), name='helloworld'),
path('posts/', PostView.as_view(), name='posts'),
path('post/<int:pk>/', PostDetailView.as_view(), name ='post_detail'),
path('posts/new/',PostCreateView.as_view(), name = 'make_post'),
path('post/update/<int:pk>/', PostUpdateView.as_view(), name ='post_update'),
path('post/delete/<int:pk>/', PostDeleteView.as_view(), name ='post_delete'),
path('like', addLike, name ='addLike'),
]