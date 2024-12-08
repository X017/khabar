# myapp/admin.py
from django.contrib import admin
from .models import Category, Post

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category',)
    search_fields = ('category',)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'views')
    list_filter = ('category', 'created_at')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
