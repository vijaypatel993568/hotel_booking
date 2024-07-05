from django.urls import path
from bookingApp import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.home),
    path('room/', views.room),
    path('room-details/', views.room_details),
    path('about/', views.about),
    path('contact/', views.contact,name="contact"),
    path('booking/<int:room_id>', views.booking),
    path('success_booking/', views.success_booking,name="success_booking"),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)