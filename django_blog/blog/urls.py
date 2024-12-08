from django.urls import path
from . import views
from .views import (
    PostListView, 
    PostDetailView, 
    PostCreateView, 
    PostUpdateView, 
    PostDeleteView,
    PostDetailView, add_comment, CommentUpdateView, CommentDeleteView
)

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),  # For creating new posts
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),  # For updating a post
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),  # For deleting a post



     path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:post_id>/comment/new/', add_comment, name='add-comment'),
    path('comment/<int:pk>/edit/', CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),


    path('posts/<int:post_id>/comments/new/', views.CommentCreateView.as_view(), name='comment_create'),

    # URL for updating a comment
    path('comments/<int:pk>/update/', views.CommentUpdateView.as_view(), name='comment_update'),
]





