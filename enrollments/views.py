from django.shortcuts import render
from emaillists.models import Emaillist
from django.contrib import messages
from django.core.mail import send_mail
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Enrollment

# Create your views here.

def listing(request, listing_id):
    listing = get_object_or_404(Enrollment, pk=id)
    context= {'listing':listing}
    return render(request, 'enrollments/listing.html', context)