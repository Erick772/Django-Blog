from django.contrib import admin

from .models import Category, Post

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'order']
    list_editable = ['order']
    ordering = ['order']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'pub_date', 'author']
    list_editable = ['pub_date']
    list_filter = ['pub_date']
    ordering = ['pub_date']
    exclude = ['author']    # O admin salvará o autor da postagem automaticamente (usuário logado)

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)
