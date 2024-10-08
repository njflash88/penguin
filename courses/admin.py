from django.contrib import admin

# Register your models here.
from .models import Course
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'catagory', 'keyword', 'instructor_id', 'price',
             'deadline', 'start_date', 'end_date', 'current_enrollment', 'max_enrollment', 'location')
    list_display_links = ('title', )
    list_filter = ('keyword','catagory', 'location')
    list_editable = ('price','current_enrollment', 'max_enrollment')
    search_fields = ('title', 'catagory', 'location', 'price')
    list_per_page = 25
    
admin.site.register(Course, CourseAdmin)