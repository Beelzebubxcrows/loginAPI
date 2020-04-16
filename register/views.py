from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from register.forms import userform

def register(request):

    if request.method =="POST":
        form= userform(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect("/success")
            
    else:
        form = userform()

    return render(request, "register.html", {"form":form})


def success(request):
    
    return render(request, "success.html",)


def details(request):
    userdetails = request.user
    return render(request, "details.html",{"userdetails":userdetails})


