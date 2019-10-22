from django.contrib import admin
from blog.models import Post, Category


class CategoryInline(admin.TabularInline):
    model = Post.categories.through


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = (CategoryInline,)
    exclude = ('categories',)


class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category, CategoryAdmin)
