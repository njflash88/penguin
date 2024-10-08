from django.shortcuts import render
from emaillists.models import Emaillist
from django.contrib import messages
from django.core.mail import send_mail
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Enrollment
from students.models import Student
from courses.models import Course

# Create your views here.

def listing(request, listing_id):
    listing = get_object_or_404(Enrollment, pk=id)
    context= {'listing':listing}
    return render(request, 'enrollments/listing.html', context)

def enroll(request, course_id):
    if request.user.is_authenticated:
        user_id = request.user.id
    else:
        return redirect('/')
    
    print("*** request.user.username",request.user.username )
    #create enrollment record
    course = get_object_or_404(Course, pk=course_id)
    #student = get_object_or_404(Student, pk=user_id)

    print("***course=", course_id, "   user_id=", user_id, request.user.username)
    if request.method == 'POST':
        #check user authenticated or not
        enrollment=Enrollment.objects.create(
        student = request.user.username,
        course=course.title
        )
        if enrollment:
            messages.success(request,f'You are now enrolled in: {course}')
        else:
            messages.error(request,'Enrollment failed!')
        return redirect(reverse('students:dashboard'))
    else:
        return render(request,'enrollments/enroll.html')
    
    