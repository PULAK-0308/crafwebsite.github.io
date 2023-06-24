from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.template import loader
from datetime import datetime
from .models import DreamProduct,ResinProduct

# Create your views here.

def index(request):
    
    return render(request,'index.html')

def signup(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Password not matched with confirm password")
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect("/")
        
    return render(request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None :
            login(request,user)
            return redirect("mainpage")
        
        else:
            return HttpResponse("password or username is incorrect") 
         
     

def mainpage(request):
    return render(request,'mainpage.html')

def dreamcatchers(request):
    products=DreamProduct.objects.all()
    print(products)
    return render(request,'dreamcatchers.html',context={'products':products})

def resinproducts(request):
    products=ResinProduct.objects.all()
    print(products)
    return render(request,'resinproducts.html',context={'products':products})

def gallery(request):
    return render(request,'gallery.html')






    

