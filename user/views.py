from django.shortcuts import render

# Create your views here.
def userindex(request):
    return render(request, 'userindex.html')
def addbooks(request):
    return render(request, 'addbooks.html')
def cart(request):
    return render(request, 'cart.html')
def profile(request):
    return render(request, 'profile.html')