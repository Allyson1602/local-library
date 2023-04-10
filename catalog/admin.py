from django.contrib import admin

from catalog.models import Book, Author, Genre, Language, BookInstance

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(BookInstance)

