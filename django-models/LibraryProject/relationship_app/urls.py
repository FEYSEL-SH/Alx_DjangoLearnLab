# relationship_app/urls.py
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView  # Import LoginView and LogoutView
from . import views  # Import your custom views

urlpatterns = [
    # URL pattern for function-based view (List all books)
    path('books/', views.list_books, name='list_books'),

    # URL pattern for class-based view (Library detail)
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    # URL patterns for user authentication using class-based views
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),  # Login view
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),  # Logout view


    # User registration view (still using function-based view in this case)
     path('register/', views.register, name='register'),  # Registration view



     path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),
]
