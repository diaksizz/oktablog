from django.contrib import admin

# Register your models here.
from .models import Posts,Category,Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_at')
    list_filter = ("published",'created_at')
    search_fields = ['title','author']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Posts,PostAdmin)
admin.site.register(Category)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']
 
    def approve_comments(self, request, queryset):
        queryset.update(active=True)