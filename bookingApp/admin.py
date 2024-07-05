from django.contrib import admin
from .models import Customer,Hotel,Room,Booking
# Register your models here.
admin.site.register((Customer,Hotel,Room,Booking))