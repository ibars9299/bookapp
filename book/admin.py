from django.contrib import admin
from .models import Book, Category

class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'author', 'page']
    search_fields = ['name', 'author']
    filter_horizontal = ['categories']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Book, BookAdmin)
admin.site.register(Category, CategoryAdmin)
