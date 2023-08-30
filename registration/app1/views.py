from django.shortcuts import render, HttpResponse ,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.core.exceptions import ValidationError
from .models import Child
# from django.contrib import admin

# admin.site.register(User)

def index(request):
    # View logic for the index page
    return render(request, 'index.html')
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib import messages

def signup(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
       
        if pass1 != pass2:
            return HttpResponse("Your password and confirm password do not match")
        else:
            # Check if the username or email already exists
            if User.objects.filter(Q(username=uname) | Q(email=email)).exists():

                # return HttpResponse("Username or email id already exists")
                messages.error(request, "Username or email already exists")
            else:
                my_user = User.objects.create_user(uname, email, pass1)
                my_user.save()
                messages.success(request, "Your account has been successfully created")
                return redirect('login')
            
    # View logic for the signup page
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)

        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password")

    # View logic for the login page
    return render(request, 'login.html')

@login_required(login_url='login')
def home(request):
    # View logic for the home page
    return render(request, 'home.html')
def Logout(request):
    logout(request)
    return redirect('index')
# views.py
from app1.models import UserRegistration

# def signup2(request):
#     if request.method == 'POST':
#         username = request.POST.get('username2')
#         email = request.POST.get('email2')
#         password1 = request.POST.get('password3')
#         password2 = request.POST.get('password4')

#         if password1 != password2:
#             return HttpResponse("Your password and confirm password do not match")
#         else:
#             # Check if the username or email already exists in the separate user registration model
#             if UserRegistration.objects.filter(username=username).exists() or UserRegistration.objects.filter(email=email).exists():
#                 messages.error(request, "Username or email already exists")
#             else:
#                 user_registration = UserRegistration(username=username, email=email, password=password1)
#                 user_registration.save()
#                 messages.success(request, "Your account has been successfully created")
#                 return redirect('login2')

#     return render(request, 'signup2.html')

# def signup2(request):
#     if request.method=='POST':
#         username=request.POST.get('username2')
#         email=request.POST.get('email2')
#         password1=request.POST.get('password3')
#         password2=request.POST.get('password4')
       
#         if password1!=password2:
#             return HttpResponse("Your password and confirm password does not match")
#         else:
#             # Check if the username or email already exists
#             if User.objects.filter(Q(username=uname) | Q(email=email)).exists():

#                 # return HttpResponse("Username or email id already exists")
#                 messages.error(request, "Username or email already exists")
#             else:
#                 my_user = User.objects.create_user(uname, email, pass1)
#                 my_user.save()
#                 messages.success(request, "Your account has been successfully created")
#                 return redirect('login2')
            
#     # View logic for the signup page
#     return render(request, 'signup2.html') 
    
def login2(request):
    # if request.method=='POST':
    #     username=request.POST.get('username')
    #     pass1=request.POST.get('pass')
    #     user=authenticate(request,username=username,password=pass1)
    #     if user is not None:
    #         auth_login(request,user)
    #         return redirect('home')
    #     else:
    #         return HttpResponse("Username or Password is incorrect")

    # View logic for the login page
    return render(request, 'login2.html')
def home2(request):
    # View logic for the home page
    return render(request, 'home2.html')
def form(request):
    if request.method=='POST':
        childName=request.POST.get('childname')
        age=request.POST.get('age')
        city=request.POST.get('city')
        remarks=request.POST.get('Remarks')
        picture=request.FILES.get('photo')

        child=Child(child_name=childName,age=age,city=city,remarks=remarks,picture=picture)
        child.save()
        messages.success(request, 'Form filled successfully .')
        # conditions

    return render(request,'form.html')

