from django.contrib import admin

# Register your models here.
from .models import Enrollment
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'enrollment_date', 'paid', 'finished',
             'passed', 'withdrawn')
    list_display_links = ('student', 'course')
    list_filter = ('student','course')
    list_editable = ('paid', 'passed')
    search_fields = ('student', 'course' )
    list_per_page = 25
    
admin.site.register(Enrollment, EnrollmentAdmin)