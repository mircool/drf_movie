from django.contrib import admin

from .models import Category, Movie


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']


class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'release_year', 'director', 'scriptwriter', 'actors', 'region']
    search_fields = ['name', 'category', 'release_year', 'director', 'scriptwriter', 'actors', 'region']
    list_filter = [ 'category', 'release_year', 'director', 'scriptwriter', 'actors', 'region']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Movie, MovieAdmin)
