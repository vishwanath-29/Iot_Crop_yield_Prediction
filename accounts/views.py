from django.shortcuts import render,redirect
from .models import User as U
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User as Usr
# Create your views here.


def login(request):
    if request.method =="POST":
        username = request.POST['username']
        passwd = request.POST['password']

        print(username)
        print(passwd)

        user = authenticate(request,email=username,password=passwd)
        print(user)
        if user is not None:
            login(request,user)
            print("successs")
            return redirect("www.google.com")
        else:
            redirect("/")

    return render(request,'accounts/login.html')

def register(request):
    if request.method == "POST":
        full_name = request.POST["full_name"]
        email_id = request.POST["email"]
        phone_number = request.POST["phone_number"]
        passwd = request.POST["password"]
        confirm_passwd = request.POST["confirm_password"]

        print(full_name)
        print(email_id)
        print(phone_number)
        print(passwd)
        print(confirm_passwd)

        user_details = U(name=full_name,email=email_id,phone_no=phone_number,password = passwd,confirm_password=confirm_passwd)
        user_details.save()

        user = Usr(email=email_id,password=passwd)
        user.save()

        return redirect('/')

    return render(request,'accounts/register.html')