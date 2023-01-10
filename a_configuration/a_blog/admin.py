from django.contrib import admin
from .models import Blog


@admin.register(Blog)# регистрируем нашу модель в админке
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date')