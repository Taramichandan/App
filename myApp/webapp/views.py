from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages

def home(req):
    if req.method == 'POST':
        username = req.POST['username']
        password = req.POST['password']

        user = authenticate(req , username = username , password = password)

        if user is not None:
            login(req,user)
            messages.success(req,'You are now logged in')

        else:
            messages.error(req,'Invalid username or password')    
            return redirect('home')
            
    return render(req,'index.html' , {})


def login_view(req):
    pass

def logout_view(req):
    logout(req)
    messages.success(req,"You are successfully logout")

    return redirect('home')
