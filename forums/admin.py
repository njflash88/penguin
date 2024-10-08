from django.contrib import admin
from .models import Forum
# Register your models here.
from .models import Forum, Post

class ForumAdmin(admin.ModelAdmin):
    list_display = ('created_by','title', 'keywords', 'created_at', 'message', 'purge')
    list_display_links = ( 'title', 'keywords')
    list_filter = ('created_by','title', 'keywords')
    list_editable = ('purge', )
    search_fields = ('created_by', 'title', 'keywords' )
    list_per_page = 25
    
admin.site.register(Forum, ForumAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ('posted_by','forum', 'content', 'created_at', )
    list_display_links = ( 'posted_by',)
    list_per_page = 20
    
admin.site.register(Post, PostAdmin)