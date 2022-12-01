from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def logout(request):
    auth.logout(request)
    return redirect('/')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid username or password")
            return redirect('login')
    return render(request,"login.html")
def register(request):
    if request.method=='POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        secondname = request.POST['secondname']
        emailid = request.POST['emailid']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username taken")
                return redirect('register')
            elif User.objects.filter(email=emailid).exists():
                messages.info(request,"email taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, first_name=firstname, last_name=secondname, email=emailid, password=password)
                user.save();
                print("user created")
                return redirect('login')
        else:
            messages.info(request,"passwords do not match")
            return redirect('register')


    return render(request,'register.html')



