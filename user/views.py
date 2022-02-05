from django.shortcuts import render,redirect,HttpResponse
from accounts.models import Userreg
from django.db import connections
from django.urls import path
from django.contrib import messages
from user.models import Books



def userindex(request):
    cm=request.session['email']
    profiles=Userreg.objects.all()
    profiles=Userreg.objects.filter(email=cm)


    displays=Books.objects.all()
    #displays=Books.objects.filter(userid=cm)
    if request.method == 'POST':
     product_id=request.POST.get('pid')
     seller_id=request.POST.get('sid')
     if seller_id == cm:
          messages.error(request,"Can't Order Your Product I tself")
     else:
         
        messages.success(request,"Product Added to Cart")
        return render(request, 'cart.html',{'profile':profiles})
    return render(request, 'userindex.html',{'display':displays})
    #return render(request, 'userindex.html',{'profile':profiles})
    
def addbooks(request):
    cm=request.session['email']
    profiles=Userreg.objects.all()
    profiles=Userreg.objects.filter(email=cm)

    if request.method == 'POST':
          
          bookname = request.POST.get('bookname')
          bookauthor = request.POST.get('bookauthor')
          description = request.POST.get('description')
          price = request.POST.get('price')
          image = request.POST.get('image')
          sr = request.POST.get('sr')
          
          bookadd=Books()


          bookadd.bookname = request.POST.get('bookname')
          bookadd.bookauthor = request.POST.get('bookauthor')
          bookadd.description = request.POST.get('description')
          bookadd.image = request.POST.get('image')
          bookadd.price = request.POST.get('price')
          bookadd.sr = request.POST.get('sr')
          bookadd.userid=cm
          bookadd.save()
          return render(request, 'addbooks.html',{'profile':profiles}) 
    else:

     return render(request, 'addbooks.html',{'profile':profiles})

def cart(request):
    cm=request.session['email']
    profiles=Userreg.objects.all()
    profiles=Userreg.objects.filter(email=cm)
    
    return render(request, 'cart.html',{'profile':profiles})

def profile(request):
    cm=request.session['email']
    profiles=Userreg.objects.all()
    profiles=Userreg.objects.filter(email=cm)

    return render(request, 'profile.html',{'profile':profiles})
def logout(request):
    try:
      del request.session['email']
    except:
        return render(request, 'index.html')
    return render(request, 'index.html')
    