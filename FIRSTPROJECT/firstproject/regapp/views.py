
from django.contrib import messages, auth
from django.shortcuts import render, redirect


# Create your views here.
def register(request):
    if request.method=="POST":
        username=request.POST['username']
        firstname=request.POST['first_name']
        lastname=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        if password==cpassword:
            from django.contrib.auth.models import User
            if User.objects.filter(username=username).exists():
                messages.info(request," This Username is not available")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request," This Email is already exist")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=email,password=password)
                user.save()
                return redirect('login')

        else:
            messages.info(request,"Password Doesn't Match")
            return redirect('register')
        return redirect('/')
    return render(request,'register.html')
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password= request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid username or password")
            return redirect('login')
    return render(request, 'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')


