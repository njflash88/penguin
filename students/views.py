# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth
from .models import Student

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
                    # add var to context dictionary
                    student_context= {
                        "street":street,
                        "city":city,
                        "district":district,
                        "country":country,
                        "postal":postal,
                        "start_date":start_date,
                        "em_contact_name":em_contact_name,
                        "em_contact_tel":em_contact_tel}
                    print("*** User.object.create_user")
                    user = User.objects.create_user(
       #             student = Student.objects.create(
                        username=username,
                        password=password,
                        first_name=first_name,
                        last_name=last_name,
                        email=email,
                        # additional fields below
        #                street=street,
        #                city=city,
        #                district=district,
        #                country=country,
        #               postal=postal,
        #                start_date=start_date,
        #                em_contact_name=em_contact_name,
        #                em_contact_tel=em_contact_tel
                        )
                    print("** before save")
                    user.save()
        #            student.save()
                    messages.success(request,'You are now registered and can log in')
                    return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
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
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request,'students/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
    return redirect("index")

def dashboard(request):
    return render(request, 'students/dashboard.html')
