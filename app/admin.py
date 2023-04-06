from django.contrib import admin

from .models import Category, TreeMenu


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Класс для отображения указанных полей
     ModelAdmin в административной панели
     """

    fields = ['name']
    list_display = ['__str__']


@admin.register(TreeMenu)
class TreeMenuAdmin(admin.ModelAdmin):
    """Класс для отображения указанных полей
    TreeMenu в административной панели
    """

    fields = ['name', 'category', 'path', 'parent']
    list_display = ['__str__', 'category', 'path', 'parent']
