
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("bookingApp.urls")),
    path('authapp/', include("authapp.urls")),
]
