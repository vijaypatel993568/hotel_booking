from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from authapp import views
urlpatterns = [
    path("login/",views.login_page,name="login"),
    path("logout/",views.logout_page),
    path("signup/",views.signup_page),
    path("profile/",views.user_profile),
    path("update-profile/",views.update_profile),
    path("forget-password/",views.forget_password),
  
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)