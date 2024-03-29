from django.contrib.auth import login as auth_login
from django.urls import path
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate
from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from accounts.models import Userreg,Login


def login(request):

     if request.method == 'POST':
        try:
            
            userdetails = Login.objects.get(email=request.POST['email'],password=request.POST['password'])
        
            print("username",userdetails)
            request.session['email']=userdetails.email
            return render(request, 'userindex.html' )
        except ObjectDoesNotExist:
            messages.success(request,"Invalid Username/Password ") 
     return render(request, 'login.html')


def register(request):
    
    if request.method == 'POST':
          
          firstname = request.POST.get('firstname')
          lastname = request.POST.get('lastname')
          address = request.POST.get('address')
          phone = request.POST.get('phone')
          email = request.POST.get('email')
          
          savecard=Userreg()
          
          savecard.firstname=request.POST.get('firstname')
          savecard.lastname=request.POST.get('lastname')
          savecard.address=request.POST.get('address')
          savecard.phone=request.POST.get('phone')
          savecard.email=request.POST.get('email')
          if Userreg.objects.filter(email=email).exists():
                 messages.success(request,'Email/Username Already Exist...')
                 return redirect('accounts:register')
          else:
           savecard.save()
    
          
          email = request.POST.get('email')
          password1 = request.POST.get('password1')
          type = request.POST.get('type')
          status=request.POST.get('status')
          login=Login()
          login.email=request.POST.get('email')
          login.password=request.POST.get('password1')
          login.type='user'
          login.status='approved'
          login.save()

          messages.success(request,"New User Created Succesfully..Please Login")
          return render(request,'login.html')    
    else:
      return render(request,'register.html')