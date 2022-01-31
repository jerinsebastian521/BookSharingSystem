from django.urls import path
from . import views

app_name = 'user'
urlpatterns = [

    
    path("userindex",views.userindex,name="userindex"),
    path("addbooks",views.addbooks,name="addbooks"),
    path("cart",views.cart,name="cart"),
    path("profile",views.profile,name="profile"),

    
    
]