
from django.shortcuts import render
from django.http import HttpResponse


def HomePage(request):
    
    return render(request, 'index.html')
#def Login(request):
    #return render(request,'login.html')
    



      
