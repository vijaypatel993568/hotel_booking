from django.shortcuts import render,redirect
from .models import Hotel,Room,Booking,Customer,Contact
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib import messages
#email related library
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

# Create your views here.
def home(request):
    latest_room=Room.objects.all()[0:5]
    return render(request,"index.html",{'latest_room':latest_room})


def room(request):
    if request.method =="POST":
        city=request.POST.get("city")
        # hotel_details=Hotel.objects.filter(city=city).id
        # print("hotel details",hotel_details)
        all_rooms=Room.objects.filter(hotel__city=city)
        return render(request,"rooms.html",{"all_rooms":all_rooms})
    else:
        all_rooms=Room.objects.all()[:8]
        return render(request,"rooms.html",{"all_rooms":all_rooms})


def room_details(request):
    return render(request,"room-details.html")


def about(request):
    return render(request,"about.html")


def contact(request):
    if request.method == "POST":
        name=request.POST.get("name")
        phone=request.POST.get("phone")
        email=request.POST.get("email")
        message=request.POST.get("message")
        Contact.objects.create(name=name,phone=phone,email=email,message=message)
        messages.success(request,"Your request successfully submitted ,our team contact as soon as possible!!!")
        return redirect("contact")
    return render(request,"contact.html")

@login_required(login_url="/authapp/login")
def booking(request,room_id):
    print("hhhhh",request.user.username)
    customer_data=Customer.objects.filter(username=request.user.username).first()
    room_data=Room.objects.get(id=room_id)
    print("room data",room_data.hotel.manager_name)
    if request.method == "POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        check_in=request.POST.get("check-in")
        check_out=request.POST.get("check-out")
        phone=request.POST.get("phone")
        person=request.POST.get("person")
    
        booking_data=Booking.objects.create(room_no=room_data,user_id=customer_data,check_in=check_in,check_out=check_out,person=person)
        print("booking data",booking_data.check_in)
        # email send for Customer regarding to booking details
        subject = 'Cogratulations Your booking have successfully executed!!!'
        html_content = render_to_string('email_template/booking_details.html', {'customer_data':customer_data,"room_data":room_data,'booking_data':booking_data})
        text_content = strip_tags(html_content)
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [customer_data.email,]
        msg = EmailMultiAlternatives(subject, text_content, email_from,recipient_list)
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        return redirect("success_booking")
    return render(request,"booking.html",{"customer_data":customer_data})

def success_booking(request):
    return render(request,"success_booking.html")
