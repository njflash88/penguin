# Create your views here.
from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
from django.contrib import messages, auth
from .models import Student
from enrollments.models import Enrollment
from courses.models import Course
from forums.models import Forum
from authuser.models import User

# Create your views here.
student_context={}

def register(request):
    print("*** in Students register")
    if request.method == 'POST':
        print("*** in Students register - POST")
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        street = request.POST['street']
        city = request.POST['city']
        district = request.POST['district']
        country = request.POST['country']
        postal = request.POST['postal']
        start_date = request.POST['start_date']
        em_contact_name = request.POST['ename']
        em_contact_tel = request.POST['ephone']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request,'Username already exists')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'Email is being used!')
                    return redirect('register')
                else:
                    print("*** User.object.create_user")
                    user = User.objects.create_user(
                        username=username,
                        password=password,
                        first_name=first_name,
                        last_name=last_name,
                        email=email,
                        is_staff=True,
                        )
                    #user.save()
                    print("** after User.object.create_user()")
                    student = Student(
                        username = user,
                        last_name=last_name,
                        first_name=first_name,
                        email=email,
                        phone=phone,
                        street=street,
                        city=city,
                        district=district,
                        country=country,
                        postal=postal,
                        start_date=start_date,
                        em_contact_name=em_contact_name,
                        em_contact_tel=em_contact_tel
                    )
                    student.save()
                    messages.success(request,'You are now registered and can log in')
                    return redirect('students:login')
        else:
            messages.error(request, 'Passwords do not match')
            return render(request, 'students/register.html')
            #return redirect('register')
    elif request.method == 'GET':
        print("*** in Students register GET")
        return render(request, 'students/register.html')
    else: print("** error in Students views ")

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('students:dashboard')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('students:login')
    else:
        return render(request,'students/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
    return redirect("/")

def dashboard(request):
    enrolled_listing = Enrollment.objects.order_by('-enrollment_date')
    print("*** in students.dashboard")
    #the following 3 filters assuming incoming html has set search criteria
    if 'created_by' in request.GET:
        created_by = request.GET['created_by']
        if created_by:
            enrolled_listing = enrolled_listing.filter(created_by__iexact=created_by)
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            enrolled_listing = enrolled_listing.filter(keyword__icontains=keyword)
    if 'discussion_title' in request.GET:
        discussion_title = request.GET['discussion_title']
        if keyword:
            enrolled_listing = enrolled_listing.filter(discussion_title__icontains=discussion_title)

    course_listing = Course.objects.order_by('id')
    forum_listing = Forum.objects
    context = { 'enrolled':enrolled_listing, 'courses':course_listing, 'forum':forum_listing}
    return render(request, 'students/dashboard.html', context)