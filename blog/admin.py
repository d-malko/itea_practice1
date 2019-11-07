from django.contrib import admin
from .models import Comment, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list = '__all__'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list = '__all__'


