# from django.contrib import admin
# from .models import Book

# admin.site.register(Book)


# class BookAdmin(admin.ModelAdmin):

#     list_display = ('title', 'author', 'publication_year')

#     search_fields = ['title', 'author']

#     list_filter = ('author', 'publication_year')

# admin.site.register(Book, BookAdmin)

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("date_of_birth", "profile_photo")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("email", "date_of_birth", "profile_photo")}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
