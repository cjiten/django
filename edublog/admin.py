from django.contrib import admin

# Register your models here.
from .models import  Web, Category, Post

class Weba(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_date')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
admin.site.register(Web, Weba)

class Categorya(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_date')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
admin.site.register(Category, Categorya)

class Posta(admin.ModelAdmin):
    list_display = ('id', 'name', 'board_name_short', 'author', 'modified_date', 'created_date')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name', 'board_name_short')
admin.site.register(Post, Posta)