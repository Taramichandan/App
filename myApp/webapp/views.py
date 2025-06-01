from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
from .forms import Registration , AddClientform
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

def client(req,pk):
    if req.user.is_authenticated:
        # look up the specific client data
        client_record = Client.objects.get(id=pk)
        return render(req,'client.html',{'client_record': client_record})
    
    else:
        messages.success(req,' You have to login......')
        return redirect ('home')
    

def client_delet(req,pk):
    if req.user.is_authenticated:
        delet_record = Client.objects.get(id=pk)
        delet_record.delete()
        messages.success(req, " You have successfully deleted")
        return redirect('home')    
    
    else : 
        messages.success(req,' YOu need to login first ...')
        return redirect('home')


def client_update(req , pk):
    if req.user.is_authenticated : 
        current_record = Client.objects.get(id=pk)
        form = AddClientform(req.POST or None , instance = current_record)
        if req.method == 'POST':
            if form.is_valid :
                update_client = form.save()
                messages.success(req , 'Client info updated ..... ')
                return redirect('home')
        return render(req, 'client_update.html' , {'form' : form})
    
    else:
        messages.success(req , 'You have to login first .....')
        return redirect('home')
    

    
def add_client(req):

    form = AddClientform(req.POST or None)

   
    if req.user.is_authenticated:
        
        if req.method == 'POST':
            if form.is_valid():  # <-- fixed here
                client = form.save(commit=False)
                client.user = req.user  # assuming Client model has a `user` field
                client.save()
                messages.success(req, 'You have successfully added the new record ......')
                return redirect('home')
        return render(req, 'add_client.html', {'form': form})  # render if not POST or form invalid

    else:
        messages.success(req, 'You have to login to add new record .......')
        return redirect('home')
       