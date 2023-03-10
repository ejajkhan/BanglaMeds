from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.conf import settings
from django.contrib.auth import authenticate,login,logout
from shop.models import Disease,Medtype
from shop.views import home

 

def signUp(request):
    medTypes = Medtype.objects.all()
    diseases = Disease.objects.all()
    params={'diseases':diseases,'medTypes':medTypes}
    return render(request,'signUp.html',params)

def logIn(request):
    medTypes = Medtype.objects.all()
    diseases = Disease.objects.all()
    params={'diseases':diseases,'medTypes':medTypes}   
    return render(request,'logIn.html',params)    

def logOut(request):   
    logout(request) 
    return redirect('logIn')

def logInAttempt(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_obj = User.objects.filter(username = username).first()
        if user_obj is None:
            messages.success(request, 'User not found.')
            return redirect('logIn')

        user = authenticate(username = username , password = password)
        if user is None:
            messages.success(request, 'Wrong password.')
            medTypes = Medtype.objects.all()
            diseases = Disease.objects.all()
            params={'diseases':diseases,'medTypes':medTypes}
            return render(request , 'logIn.html',params)
        
        login(request , user)
        return redirect(home)
    medTypes = Medtype.objects.all()
    diseases = Disease.objects.all()
    params={'diseases':diseases,'medTypes':medTypes}
    return render(request , 'logIn.html',params)

def signUpConfirmation(request):
    if request.method=='POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        retypePassword = request.POST.get('retypePassword') 
        if User.objects.filter(username = username).first(): 
            messages.success(request, 'This username is taken before.')
            return redirect('signUp')

        if User.objects.filter(email = email).first(): 
            messages.success(request, 'This email is already in used.')
            return redirect('signUp')

        if password!=retypePassword:
            messages.success(request, "Re-entered password doesn't match.")
            return redirect('signUp')
        if len(password)<8:
            messages.success(request, "Password is too short.")
            return redirect('signUp')
        obj = User.objects.create(username=username,email=email)
        obj.set_password(password)
        obj.save() 
    medTypes = Medtype.objects.all()
    diseases = Disease.objects.all()
    params={'diseases':diseases,'medTypes':medTypes}
    return render(request , 'logIn.html',params)
  
