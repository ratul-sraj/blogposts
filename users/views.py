from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
# Create your views here.

def register(req):
    if req.method == "POST":
        form = UserRegisterForm(req.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(req, f"Your Account Has been created  Please Log in !")
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(req, "users/register.html", {"form": form})

@login_required()
def profile(req):
    return render(req,"users/profile.html")