from django.shortcuts import render , redirect
from django.contrib.auth import login , logout , authenticate
from django.contrib.auth.decorators import login_required
from .forms import userform , userauthentication
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
# Create your views here.

def main_page(request) : 
     return render(request , 'app1/main.html')

def sign_up_page (request) : 
    if request.method == "POST" :
        form = userform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app1:main')
        else :
            for error in form.errors.values():
                messages.error(request , error)
    else :
        form = userform()
    return render(request , 'app1/sign_up.html', { 'form' : form})

def login_page (request) :
    if request.method == "POST" :
        form = userauthentication(request , data = request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request , username = username , password = password)
            if user is not None :
                return redirect('app1:main')
            else :
                messages.error(request , "login error")
        else :
            messages.error(request , 'login error')
    else :
        form = userauthentication()
    return render(request , "app1/login_page.html" , {'form' : form})


    

    
    


