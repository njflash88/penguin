from django.shortcuts import render
from django.contrib import messages
from courses.models import Course
from authuser.models import User
from enrollments.models import Enrollment
from students.models import Student
from datetime import timedelta
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils import timezone


# Create your views here.
def index(request):
    courses = Course.objects.order_by('id')
    context = {'courses': courses}
    return render(request, 'courses/listings.html', context )

def listing(request, course_id):
    #course = Course.objects.get(id=course_id)
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'courses/listing.html', {'course':course})

def enroll(request, course_id):
    #create enrollment record
    print("*** IN COURSE.ENROLL")
    course = get_object_or_404(Course, pk=course_id)
    print("*** User.username=" , User.username)
    if request.method == 'POST':
        enrollment=Enrollment.objects.create(
        student = User.username,
        course=course.title,
        )
    if enrollment:
            messages.success(request,'You are now enrolled to:', course_id )
    else:
        messages.error(request,'Enrollment failed!')
#    return render(request, 'courses/enroll.html')
    return redirect(reverse('students:dashboard'))