from django.contrib import admin

# Register your models here.
from .models import Instructor
class InstructorAdmin(admin.ModelAdmin):
    list_display = ('lastname', 'firstname', 'phone', 'email', 'street',
             'city', 'district', 'country', 'postal', 'start_date', 'background', 'em_contact', 'em_tel')
    list_display_links = ('lastname', 'firstname')
    list_filter = ('lastname','firstname')
    list_editable = ('email', 'background')
    search_fields = ('lastname', 'firstname' )
    list_per_page = 25
    
admin.site.register(Instructor, InstructorAdmin)