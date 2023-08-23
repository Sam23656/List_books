from django.contrib import admin
from Books.models import Book, Author, Genre


# Register your models here.

class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'Slug': ('Name',)
    }


admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Genre)
