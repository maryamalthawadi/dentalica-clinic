from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('home.html', views.home, name="home"),
    path('service.html', views.service, name="service"),
    path('contact.html', views.contact, name="contact"),
    path('contactform.html', views.contactform, name="contactform"),
    path('booking.html', views.booking, name="booking"),
    path('bookingform.html', views.bookingform, name="bookingform"),
    path('call.html', views.call, name="call"),
    path('callform.html', views.callform, name="callform"),
]
