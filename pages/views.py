from django.shortcuts import render
from django.http import HttpResponse
from courses.models import Course

# Create your views here.

def index(request):
    courses = Course.objects.order_by('id')
    print("courses=", courses)
    context = {'courses': courses}
    return render(request, 'pages/index.html', context )

def about(request):
    return render(request, 'pages/about.html')