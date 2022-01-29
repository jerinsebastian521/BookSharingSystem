from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
# Create your views here.

def register(request):
    
    if request.method == 'POST':

          first_name = request.POST.get('first_name')
          last_name = request.POST.get('last_name')
          username = request.POST.get('username')
          password1 = request.POST.get('password1')
          password2 = request.POST.get('password2')
          email = request.POST.get('email')

          if password1 == password2:
                if User.objects.filter(username=username).exists():
                      messages.info(request,'Username Taken')
                      return redirect('/accounts/register')
                elif User.objects.filter(email=email).exists():
                     
                      return redirect('/accounts/register')
                      messages.info(request,'Email Taken')
                else:
                  user= User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                  user.save()
                  print('user created')
          else:
            print('Password Not Matching...')   
            return redirect('/accounts/register')
          return redirect('/login/')
          
    else:
       return render(request,'register.html')