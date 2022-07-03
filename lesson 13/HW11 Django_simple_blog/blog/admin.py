from django.contrib import admin

from .models import *


class PostAdmin(admin.ModelAdmin):
    list_display = 'id', 'title',
    list_display_links = 'id', 'title',
    search_fields = 'title',
    prepopulated_fields = {'slug': ('title',)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = 'id', 'name',
    list_display_links = 'id', 'name',
    search_fields = 'name',
    prepopulated_fields = {'slug': ('name',)}
    list_filter = 'id',


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
