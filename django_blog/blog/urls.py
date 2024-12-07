from .views import register
from django.urls import path
from . import views


urlpatterns = [
    path('register/', register, name='register'),
    path('profile/', views.profile, name='profile'),
]
