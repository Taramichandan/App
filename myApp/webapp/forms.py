from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Client

class Registration(UserCreationForm):
    email = forms.EmailField(required=True,label='',widget=forms.TextInput(attrs={'class' : 'form-control' , 'placeholder' : 'Email'}))
    first_name = forms.CharField(max_length=30,label='',widget=forms.TextInput(attrs={'class' : 'form-control' , 'placeholder':'First Name'}))
    last_name = forms.CharField(max_length=30,label='',widget=forms.TextInput(attrs={'class':'form-control' , 'placeholder' : 'Last Name'}))


    class Meta : 
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')

    def __init__(self, *args, **kwargs):
        super(Registration,self).__init__(*args, **kwargs)    

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Password'



# Create add client form        

class AddClientform(forms.ModelForm):
    first_name = forms.CharField(max_length=30,label='',widget=forms.TextInput(attrs={'class' : 'form-control' , 'placeholder':'First Name'}))
    email = forms.EmailField(required=True,label='',widget=forms.TextInput(attrs={'class' : 'form-control' , 'placeholder' : 'Email'}))
    phone = forms.CharField(max_length=30,label='',widget=forms.TextInput(attrs={'class' : 'form-control' , 'placeholder':'Phone'}))
    address = forms.CharField(max_length=30,label='',widget=forms.TextInput(attrs={'class' : 'form-control' , 'placeholder':'Address'}))
    city = forms.CharField(max_length=30,label='',widget=forms.TextInput(attrs={'class' : 'form-control' , 'placeholder':'City'}))
    state = forms.CharField(max_length=30,label='',widget=forms.TextInput(attrs={'class' : 'form-control' , 'placeholder':'State'}))
    zip_code = forms.CharField(max_length=30,label='',widget=forms.TextInput(attrs={'class' : 'form-control' , 'placeholder':'Zip-code'}))
    # created_at = forms.CharField(max_length=30,label='',widget=forms.TextInput(attrs={'class' : 'form-control' , 'placeholder':'Created_at'}))

    class Meta:
        model = Client 
        exclude = ('user',)