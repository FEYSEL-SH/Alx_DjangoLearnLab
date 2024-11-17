# relationship_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # URL pattern for function-based view (List all books)
    path('books/', views.list_books, name='list_books'),

    # URL pattern for class-based view (Library detail)
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]
