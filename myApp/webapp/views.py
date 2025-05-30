from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
from .forms import Registration
from .models import Client

def home(req):

    # Gap all client Records
    clients = Client.objects.all()


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
            
    return render(req,'index.html' ,{'clients' : clients})


def register_view(req):

    if req.method == 'POST' :
        form = Registration(req.POST)
        if form.is_valid():
            form.save

            username = form.cleaned_data.get('username')
            password1 = form.cleaned_data.get('password1')

            user = authenticate(username = username , password1 = password1)

            login(req,user)
            messages.success(req, 'You are successfully registerd')
            return redirect('home')
    else:
        form = Registration()
        return render(req,'register.html',{'form': form})

def logout_view(req):
    logout(req)
    messages.success(req,"You are successfully logout")

    return redirect('home')
