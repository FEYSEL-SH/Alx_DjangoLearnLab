
---

### 4. `delete.md`

```markdown
# Delete Operation

## Command
```python
from bookshelf.models import Book

# Fetch the book to delete
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()  # Deletes the book instance from the database

# Confirm deletion by trying to retrieve all books again
all_books = Book.objects.all()
print(all_books)  

# Output: <QuerySet []>
