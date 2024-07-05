from django.shortcuts import render,HttpResponseRedirect,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from bookingApp.models import Customer
#for login page that user can login 
def login_page(request):
    if request.method == "POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            request.session.set_expiry(60*60*24*30) #set session expiry time for 30 days
            if user.is_superuser:
                return HttpResponseRedirect("/admin/")
            else:
                return HttpResponseRedirect("/authapp/profile/")
        else:
            messages.error(request,'username or password are invalid!!!')
    return render(request,'login.html')
  
  
  #this is for logout page.
def logout_page(request):
    logout(request)
    return redirect("login")
    


#This is for if user forgot our password.
def forget_password(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        confirm_password=request.POST.get("confirm_password")
        if password==confirm_password:
            user=User.objects.get(username=username)
            if user is not None:
                user.set_password(password)
                user.save()
                messages.success(request,"Password updated successfully!!!")
                return redirect("login")
            else:
                messages.error(request,"Username doesn' exist!!!")
        else:
            messages.error(request,"Password and Confirm Password doesn't matched!!!")
    return render(request,"forget.html")
    


#view for new user registration.
def signup_page(request):
    
    if request.method == "POST":
        name=request.POST.get("name")
        username=request.POST.get("username")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        password=request.POST.get("password")
        confirm_password=request.POST.get("confirm_password")
        if password == confirm_password:
            user_is_exist=User.objects.filter(username=username)
            if user_is_exist:
                messages.error(request,"username already taken !!!")
                return redirect("/authapp/signup/")
            user=User.objects.create(username=username)
            user.set_password(password)
            user.save()
            obj=Customer()
            obj.name=name
            obj.username=username
            obj.phone=phone
            obj.email=email
            obj.save()
            messages.success(request,"user registered successfully Now you can login!!!")
            return redirect("/authapp/login/")
        else:
            messages.error(request,"password and confirm password does not matched!!!")
            return render(request,'signup.html')
    return render(request,'signup.html')
    

def user_profile(request):
        customer=Customer.objects.get(username =request.user.username)
        return render(request,'profile.html',{'data':customer,})


#for user's profile update.
def update_profile(request):
        user = User.objects.get(username=request.user.username)
        if(user.is_superuser):
            return HttpResponseRedirect("/admin/")
        else:
            customer = Customer.objects.get(username=request.user.username)
            if request.method=="POST":
                name=request.POST.get("name")
                email=request.POST.get("email")
                phone=request.POST.get("phone")
                address1=request.POST.get("address1")
                address2=request.POST.get("address2")
                pin=request.POST.get("pin")
                city=request.POST.get("city")
                state=request.POST.get("state")
                profile_pic=request.FILES.get("pic")
                print("profile pic",profile_pic)
                customer.name=name
                customer.email=email
                customer.phone=phone
                customer.address1=address1
                customer.address2=address2
                customer.city=city
                customer.state=state
                if profile_pic:
                    customer.profile_pic=profile_pic
                customer.save()
                return HttpResponseRedirect("/authapp/profile/")
        return render(request,"updateProfile.html",{"data":customer})
