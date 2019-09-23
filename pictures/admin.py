from django.contrib import admin
from .models import Picture
from .models import Image


class PictureAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'caption', 'owner')
    ordering = ('id',)
    search_fields = ('caption',)


class ImageAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'created_at', 'caption', 'owner', 'image')
    ordering = ('uuid',)
    search_fields = ('caption',)


admin.site.register(Picture, PictureAdmin)
admin.site.register(Image, ImageAdmin)
