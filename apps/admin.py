from django.contrib import admin
from django.contrib.admin import ModelAdmin
from parler.admin import TranslatableAdmin

from .models import ContactMessage, Category, Project, Image


@admin.register(ContactMessage)
class ContactMessageAdmin(ModelAdmin):
    list_display = ('name', 'phone', 'email', 'created_at', 'is_processed')
    list_filter = ('is_processed', 'created_at')
    search_fields = ('name', 'phone', 'email', 'message')
    readonly_fields = ('created_at',)


@admin.register(Category)
class CategoryAdmin(TranslatableAdmin):
    # Поля, которые будут отображаться в списке (непереводимые + переводимые)
    list_display = ('title', 'created_at')

    # Конфигурация полей внутри формы редактирования
    fieldsets = (
        (None, {
            'fields': ('title',),  # Переводимые поля
        }),
    )

@admin.register(Project)
class ProjectAdmin(TranslatableAdmin):
    list_display = ('title', 'category', 'created_at')

    fieldsets = (
        (None, {
            'fields': ('category', 'title', 'description'),
        }),
    )

@admin.register(Image)
class ImageAdmin(ModelAdmin):
    list_display = ('image', 'created_at')
    list_filter = ('project',)
    readonly_fields = ('created_at',)
