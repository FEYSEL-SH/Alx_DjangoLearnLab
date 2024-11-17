from django.db import models

# Author Model
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Book Model
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

# Library Model
class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name
# relationship_app/views.py
from django.views.generic import DetailView
from .models import Library

# Class-based view to display details of a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'  # Template to render
    context_object_name = 'library'  # The object to pass to the template

class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)