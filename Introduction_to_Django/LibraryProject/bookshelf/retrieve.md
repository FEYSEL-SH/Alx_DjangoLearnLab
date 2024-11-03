
---

### 2. `retrieve.md`

```markdown
# Retrieve Operation

## Command
```python
from bookshelf.models import Book

# Retrieve and display all attributes of the book created earlier
all_books = Book.objects.all()
for book in all_books:
    print(book.title, book.author, book.publication_year)  
    
    
# 1984 George Orwell 1949
