from django.contrib import admin

# Register your models here.
from .models import Emaillist
class EmaillistAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'subscribe_date', 'purge')
    list_display_links = ('name', 'email')
    list_filter = ('name','email')
    list_editable = ('purge', )
    search_fields = ('name', 'email' )
    list_per_page = 25
    
admin.site.register(Emaillist, EmaillistAdmin)