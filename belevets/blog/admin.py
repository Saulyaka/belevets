from django.contrib import admin

from .models import Blog, Comment


@admin.register(Blog)
class AdminBlog(admin.ModelAdmin):
    pass


@admin.register(Comment)
class AdminComment(admin.ModelAdmin):
    pass
