from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.

def register(req):
    if (req.method =="POST"):
        form = UserCreationForm(req.POST)
        if form.is_valid():
            print("the form is valid")
            username = form.cleaned_data.get("username")
            messages.success(req,f"Account created for {username} !")
            return redirect("blog-home")
    else:
        form = UserCreationForm()
        return render(req,"users/register.html", {"form":form})
