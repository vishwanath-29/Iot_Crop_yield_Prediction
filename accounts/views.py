from django.shortcuts import render,redirect

# Create your views here.

def login(request):
    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']

        print(username)
        print(password)

        

        return redirect("/cropprediction")

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

        return redirect('/login')

    return render(request,'accounts/register.html')