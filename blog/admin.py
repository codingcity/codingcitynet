from django.contrib import admin
from .models import Post, Categoryblog
from markdownx.admin import MarkdownxModelAdmin

admin.site.register(Post, MarkdownxModelAdmin)


class CategoryblogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}

admin.site.register(Categoryblog, CategoryblogAdmin)