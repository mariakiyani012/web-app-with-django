from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Schedule
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        'variable1':'only one',
        'variable2':'This is sent.'
    }
    return render(request, 'index.html', context)
    #return HttpResponse("this is a homepage")

def services(request):
    return render(request, 'services.html')

def about(request):
    return render(request, 'about.html')
       
def careers(request):
    return render(request, 'careers.html')

def schedule(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        date = request.POST.get('date')
        desc = request.POST.get('desc')
        schedule = Schedule(name=name, email=email, contact=contact, date=date, desc=desc)
        schedule.save()
        messages.success(request, "Your schedule request has been submitted!")
    return render(request, 'schedule.html')

