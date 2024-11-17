# relationship_app/urls.py
from django.urls import path
from .views import list_books, LibraryDetailView, login_view, logout_view, register  # Correct import for both views

urlpatterns = [
    path('books/', list_books, name='list_books'),  # Function-based view for listing books
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # Class-based view for library detail
]


urlpatterns = [
    # URL pattern for function-based view (List all books)
    path('books/', views.list_books, name='list_books'),

    # URL pattern for class-based view (Library detail)
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

      path('login/', login_view, name='login'),  # User login
    path('logout/', logout_view, name='logout'),  # User logout
    path('register/', register, name='register'),  # User registration
]
