from django.contrib import admin
from .models import Blog
from .models import Ministry
from .models import GalleryImage
from django.utils.html import format_html

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'thumbnail')
    search_fields = ('title', 'content', 'author')
    list_filter = ('created_at', 'author')
    readonly_fields = ('preview_large',)


    def thumbnail(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width:80px; height:50px; object-fit:cover;"/>', obj.image.url)
        return '-'
    thumbnail.short_description = 'Image'

    def preview_large(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-width:300px;"/>', obj.image.url)
        return '-'
    preview_large.short_description = 'Preview'

admin.site.register(Blog, BlogAdmin)


# ministry
@admin.register(Ministry)
class MinistryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title',)


# gallery
from django.contrib import admin
from .models import GalleryImage

class GalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'image')  # ✅ remove '-uploaded_at'
    list_filter = ('category',)  # ✅ remove '-uploaded_at'

admin.site.register(GalleryImage, GalleryAdmin)