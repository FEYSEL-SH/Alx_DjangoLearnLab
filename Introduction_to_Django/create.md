# Create Operation

## Command
```python
from bookshelf.models import Book

# Create a Book instance
book = Book(title="1984", author="George Orwell", publication_year=1949)
book.save()  # Save the instance to the database

# Verification command
print("Book created:", book)  

# Output: Book created: 1984
