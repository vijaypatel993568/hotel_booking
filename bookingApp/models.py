from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model):
    name=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.CharField(max_length=12)
    address1=models.CharField(max_length=200)
    address2=models.CharField(max_length=200)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    profile_pic=models.ImageField(upload_to="profile_pic")

    def __str__(self):
        return self.name

class Hotel(models.Model):
    hotel_name=models.CharField(max_length=200)
    manager_name=models.CharField(max_length=50)
    manager_phone=models.CharField(max_length=20)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    country=models.CharField(max_length=50)
    
    def __str__(self):
        return self.hotel_name
    
    
class Room(models.Model):
    hotel=models.ForeignKey(Hotel,on_delete=models.CASCADE)
    room_no=models.CharField(max_length=5)
    room_type=models.CharField(max_length=50)
    services=models.CharField(max_length=200,default="")
    capacity=models.PositiveIntegerField(default=2)
    is_available=models.BooleanField(default=True)
    price=models.FloatField()
    pic1=models.ImageField(upload_to="room_pics")
    pic2=models.ImageField(upload_to="room_pics",default=None,null=True,blank=True)
    pic3=models.ImageField(upload_to="room_pics",default=None,null=True,blank=True)
    pic4=models.ImageField(upload_to="room_pics",default=None,null=True,blank=True)
    
    def __str__(self):
        return "Room id :"+str(self.id)

class Booking(models.Model):
    room_no=models.ForeignKey(Room,on_delete=models.CASCADE)
    user_id=models.ForeignKey(Customer,on_delete=models.CASCADE)
    check_in=models.DateField(auto_now=False, auto_now_add=False)
    check_out=models.DateField(auto_now=False, auto_now_add=False)
    person=models.CharField(max_length=200)
    booked_on=models.DateTimeField(auto_now=True, auto_now_add=False)
    def __str__(self):
        return "Booking ID:"+str(self.id)
    
class Contact(models.Model):
    name=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    email=models.EmailField()
    
    message=models.TextField()
    
    def __str__(self):
        return self.name