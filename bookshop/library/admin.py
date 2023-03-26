from django.contrib import admin
from library.models import Author, Book, Library


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name')


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publication_date')
    search_fields = ('title',)
    date_hierarchy = 'publication_date'
    fields = ('title', 'publication_date')

class LibraryAdmin(admin.ModelAdmin):
    authors = ('first_name', 'last_name')
    books = ('title', 'publication_date')


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Library, LibraryAdmin)