from django.contrib import admin
from .models import Category, Topic, Post

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'created')
    list_filter = ('name', 'category', 'created')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    readonly_fields = ('created_at',)

    list_display = ('title', 'short_text_preview', 'topic', 'slug', 'created_at', 'updated_at', 'created_by')
    list_filter = ('topic', 'created_by')
    prepopulated_fields = {"slug": ("title",)}


    def short_text_preview(self, obj):
        words = obj.text.split()
        if len(words) > 5:
            return ' '.join(words[:5]) + '...'
        else:
            return obj.text
    short_text_preview.short_description = 'Początek tekstu'