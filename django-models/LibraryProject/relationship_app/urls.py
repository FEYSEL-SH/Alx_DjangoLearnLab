# relationship_app/urls.py
from django.urls import path
from . import views  # Import all views at once

urlpatterns = [
    # URL pattern for function-based view (List all books)
    path('books/', views.list_books, name='list_books'),

    # URL pattern for class-based view (Library detail)
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    # User authentication URLs
    path('login/', views.login_view, name='login'),  # User login
    path('logout/', views.logout_view, name='logout'),  # User logout
    path('register/', views.register, name='register'),  # User registration
]
