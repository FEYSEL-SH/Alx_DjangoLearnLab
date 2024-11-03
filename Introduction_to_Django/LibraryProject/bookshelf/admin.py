from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_date')
    search_fields = ('title', 'author__name')
    list_filter = ('publication_date',)

# Register the Book model with the custom BookAdmin class
admin.site.register(Book, BookAdmin)