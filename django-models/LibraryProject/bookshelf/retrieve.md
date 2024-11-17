# Retrieve Operation

**Python Command**:
```python
book = Book.objects.get(title="1984")
print(book.title)
print(book.author)
print(book.publication_year)


# 1984
# George Orwell
# 1949
