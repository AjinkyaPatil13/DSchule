from django.shortcuts import render
from django.http import HttpResponse
from DSchule_app.models import Contact
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages


# Create your views here.
@csrf_exempt
def index(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        contact = Contact(first_name=first_name, last_name=last_name, email=email, message=message, phone=phone)
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, "index.html")
