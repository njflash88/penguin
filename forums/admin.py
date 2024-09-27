from django.contrib import admin
from .models import Forum
# Register your models here.
from .models import Forum

class ForumAdmin(admin.ModelAdmin):
    list_display = ('created_by', 'poster','discussion_title', 'keywords', 'create_date', 'message', 'purge')
    list_display_links = ( 'discussion_title', 'keywords')
    list_filter = ('created_by', 'poster','discussion_title', 'keywords')
    list_editable = ('purge', )
    search_fields = ('created_by', 'poster', 'discussion_title', 'keywords' )
    list_per_page = 25
    
admin.site.register(Forum, ForumAdmin)