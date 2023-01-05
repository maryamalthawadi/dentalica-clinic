from django.shortcuts import render
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def service(request):
    return render(request, 'service.html', {})

def contact(request):
    return render(request, 'contact.html', {})

def contactform(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        return render(request, 'contactform.html', {
        'message_name': message_name,
        'message_email': message_email,
        'message': message,
        })

    else:
        return render(request, 'contact.html', {})

def booking(request):
    return render(request, 'booking.html', {})

def bookingform(request):
    if request.method == "POST":
        your_name = request.POST['your-name']
        your_phone = request.POST['your-phone']
        your_email = request.POST['your-email']
        your_service = request.POST['your-service']
        your_day = request.POST['your-day']
        your_time = request.POST['your-time']
        your_message = request.POST['your-message']

        return render(request, 'bookingform.html', {
        'your_name': your_name,
        'your_phone': your_phone,
        'your_email': your_email,
        'your_service': your_service,
        'your_day': your_day,
        'your_time': your_time,
        'your_message': your_message
        })
    else:
        return render(request, 'booking.html', {})

def call(request):
    return render(request, 'call.html', {})

def callform(request):
    if request.method == "POST":
        your_name = request.POST['your-name']
        your_phone = request.POST['your-phone']

        return render(request, 'callform.html', {
        'your_name': your_name,
        'your_phone': your_phone,
        })
    else:
        return render(request, 'call.html', {})
