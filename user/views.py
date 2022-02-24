from django.shortcuts import render,redirect,HttpResponse
from accounts.models import Userreg
from django.db import connections
from django.urls import path
from django.contrib import messages
from user.models import Books,Bookstatus




def userindex(request):
    cm=request.session['email']
    profiles=Userreg.objects.all()
    profiles=Userreg.objects.filter(email=cm)


    displays=Books.objects.all()
    #displays=Books.objects.filter(userid=cm)
    
    if request.method == 'POST':
        
        product_id=request.POST.get('pid')
        seller_id=request.POST.get('sid')
        bname=request.POST.get('bname')

        if seller_id == cm:
             messages.error(request,"Can't Order Your Product Itself")
             return render(request, 'userindex.html',{'display':displays})
        else:
         bs=Bookstatus()
         bs.prod_id=product_id
         bs.user_id=cm
         bs.sell_id= seller_id
         bs.payment='NotSucces'
         bs.d_status='NotInitiated'
         bs.bname=bname
         bs.save()
         messages.success(request,"Product Added to Cart")
         return render(request, 'userindex.html',{'display':displays,'profile':profiles})
         
    return render(request, 'userindex.html',{'display':displays,'profile':profiles})
    
def addbooks(request):
    cm=request.session['email']
    profiles=Userreg.objects.all()
    profiles=Userreg.objects.filter(email=cm)
  
    bookdis=Books.objects.all()
    bookdis=Books.objects.filter(userid=cm)
    bst=Books.bid
    bookstat=Bookstatus.objects.all()
    bookstat=Bookstatus.objects.filter(sell_id=cm).filter(prod_id=bst)
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
          return render(request, 'addbooks.html',{'profile':profiles,'book':bookdis}) #'bookst':bookstat
    else:
    
     return render(request, 'addbooks.html',{'profile':profiles,'book':bookdis})

    if request.method == 'GET':
        return render(request, 'addbooks.html',{'profile':profiles,'book':bookdis})
    else:
        return render(request, 'addbooks.html',{'profile':profiles,'book':bookdis})

def cart(request):
    cm=request.session['email']
    profiles=Userreg.objects.all()
    profiles=Userreg.objects.filter(email=cm)

    bookd=Bookstatus.objects.all()
    bookd=Bookstatus.objects.filter(user_id=cm). filter(payment='NotSucces')

 
    
    
    if request.method == 'POST':
       prod=request.POST.get('pd')
       up=Bookstatus.objects.get(prod_id=prod)
       up.payment='Succes'
       up.save()
       return render(request, 'cart.html',{'bookdt':bookd,'profile':profiles})
    else:
      return render(request, 'cart.html',{'bookdt':bookd,'profile':profiles})

    



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
    