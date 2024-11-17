# Delete Operation on the Book Model

This document demonstrates the delete operation on the `Book` model in Django.

### Steps:

1. **Import the Book model:**
   ```python
   from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
>>> book.delete()
<!-- (1, {'bookshelf.Book': 1}) -->
