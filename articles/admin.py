from django.contrib import admin
from .models import Article


class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'owner',)
    ordering = ('id', 'owner')
    search_fields = ('content',)


admin.site.register(Article, ArticlesAdmin)
