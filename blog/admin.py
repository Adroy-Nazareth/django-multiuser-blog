from django.contrib import admin
from .models import Comment,Post,Tag
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=('title','author','published','created_at');list_filter=('published','created_at','tags');search_fields=('title','content','author__username');prepopulated_fields={'slug':('title',)}
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display=('post','author','approved','created_at');list_filter=('approved','created_at');search_fields=('body','author__username','post__title');actions=['approve_comments','reject_comments']
    @admin.action(description='Approve selected comments')
    def approve_comments(self,request,queryset):queryset.update(approved=True)
    @admin.action(description='Reject selected comments')
    def reject_comments(self,request,queryset):queryset.update(approved=False)
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display=('name','slug');search_fields=('name',)
