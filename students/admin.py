from django.contrib import admin

# Register your models here.
from .models import Student
class StudentAdmin(admin.ModelAdmin):
    list_display = ('username', 'last_name', 'first_name', 'phone', 'email',
             'street', 'city', 'district', 'country', 'postal', 'start_date', 'em_contact_name', 'em_contact_tel')
    list_display_links = ('username', )
    list_filter = ('username','last_name', 'city')
    list_editable = ('email', 'phone')
    search_fields = ('username', 'email', 'last_name')
    list_per_page = 25
    
admin.site.register(Student, StudentAdmin)