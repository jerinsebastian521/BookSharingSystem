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
def logout(request):
    try:
      del request.session['email']
    except:
        return render(request, 'index.html')
    return render(request, 'index.html')
    