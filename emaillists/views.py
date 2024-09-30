from django.shortcuts import render
from emaillists.models import Emaillist
from django.contrib import messages
from django.core.mail import send_mail
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect

# Create your views here.
def subscribe(request):
    context = request.POST
    if request.method == 'POST':
        email = context.get('email')
        print("*** email=",email)
        # update database 
        emaillistRec=Emaillist.objects.create(email=email)
        if emaillistRec:
            messages.success(request,'You are now subscribed to our news letter')
        else:
            messages.error(request,'Subscribe failed!')

    return redirect(reverse('pages:index'))
    
    

