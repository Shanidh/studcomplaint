from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.newfunction,name='index'),
    path('login',views.newfunction1,name='login'),
    path('signup',views.newfunction2,name='signup'),
    path('base',views.newfunction3,name='base'),
    path('addcomplaints',views.newfunction4,name='addcomplaints'),
    path('changepassword',views.newfunction5,name='changepassword'),
    path('editprofile',views.newfunction6,name='editprofile'),
]