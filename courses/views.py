from django.shortcuts import render
from courses.models import Course
from datetime import timedelta
from django.shortcuts import render, get_object_or_404

# Create your views here.
def index(request):
    courses = Course.objects.order_by('id')
    context = {'courses': courses}
    return render(request, 'courses/listings.html', context )

def listing(request, course_id):
    print("*** HERE in vIEW listing")
    #course = Course.objects.get(id=course_id)
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'courses/listing.html', {'course':course})
