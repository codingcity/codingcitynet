from django.contrib import admin
from .models import Post, Categoryblog

admin.site.register(Post)


class CategoryblogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}

admin.site.register(Categoryblog, CategoryblogAdmin)