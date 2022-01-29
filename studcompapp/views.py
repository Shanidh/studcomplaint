from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def newfunction(request):
    return render(request,'index.html')

def newfunction1(request):
    return render(request,'login.html')    

def newfunction2(request):
    return render(request,'signup.html') 

def newfunction3(request):
    return render(request,'base.html')  

def newfunction4(request):
    return render(request,'addcomplaints.html') 

def newfunction5(request):
    return render(request,'changepassword.html') 

def newfunction6(request):
    return render(request,'editprofile.html')   