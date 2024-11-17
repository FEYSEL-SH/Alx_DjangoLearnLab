
from .models import Book
from django.views.generic.detail import DetailView
from .models import Library

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()  # Get all books from the database
    return render(request, 'relationship_app/list_books.html', {'books': books})


# Class-based view to display details of a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  # Template to render
    context_object_name = 'library'  # The object to pass to the template


# relationship_app/views.py


# User registration view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user to the database
            login(request, user)  # Log the user in immediately after registration
            return redirect('list_books')  # Redirect to a desired page after registration
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})

# User login view
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('list_books')  # Redirect to the books listing page after login
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

# User logout view
@login_required  # Ensure that the user is logged in to access this view
def logout_view(request):
    logout(request)
    return render(request, 'logout.html')




from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render

# Helper function to check if the user has the 'Admin' role
def is_admin(user):
    return user.profile.role == 'Admin'

# Helper function to check if the user has the 'Librarian' role
def is_librarian(user):
    return user.profile.role == 'Librarian'

# Helper function to check if the user has the 'Member' role
def is_member(user):
    return user.profile.role == 'Member'

# Admin view (only accessible by Admin users)
@login_required
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

# Librarian view (only accessible by Librarian users)
@login_required
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

# Member view (only accessible by Member users)
@login_required
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')
