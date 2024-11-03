
---

### 3. `update.md`

```markdown
# Update Operation

## Command
```python
from bookshelf.models import Book

# Fetch the book to update
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"  # Change the title
book.save()  # Save the changes

# Verification command to check if the title is updated
updated_book = Book.objects.get(id=book.id)  # Fetch the updated book
print(updated_book.title)  

# Output: Nineteen Eighty-Four
