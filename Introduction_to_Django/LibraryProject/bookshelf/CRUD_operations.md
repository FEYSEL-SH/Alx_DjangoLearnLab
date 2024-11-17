# CRUD Operations on the Book Model

This document demonstrates the basic CRUD (Create, Retrieve, Update, Delete) operations on the `Book` model in Django.

---

## 1. Create Operation

### Command:
```python
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)


# >>> book
# <Book: 1984>


book = Book.objects.get(title="1984")
print(book.title)  # Expected output: "1984"
print(book.author)  # Expected output: "George Orwell"
print(book.publication_year)  # Expected output: 1949

# >>> print(book.title)
# 1984
# >>> print(book.author)
# George Orwell
# >>> print(book.publication_year)
# 1949


book.title = "Nineteen Eighty-Four"
book.save()
print(book.title)  # Expected output: "Nineteen Eighty-Four"

# >>> print(book.title)
# Nineteen Eighty-Four


book.delete()

>>> book.delete()
# (1, {'bookshelf.Book': 1})
