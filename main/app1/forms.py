from django import forms
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth.models import User

class userform (UserCreationForm) :
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder' : "Email",
    }),
    required=False
    )

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : "username",
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder' : 'password' ,
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder' : 'password confirmation'
    }))

    class Meta:
        model = User
        fields = ('username' , 'email' , 'password1' , 'password2') 


class userauthentication (AuthenticationForm) :
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : "username"
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder' : 'password'
    }))
