from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import CustomUser

# Create your views here.
def index_view(request):
    err = None
    return render(request, "index.html", {"err":err})

def register_view(request):
    if request.method == "POST":
        if request.POST["is_developer"] == "1":
            dev = 1
        else:
            dev = 0
            
        CustomUser.objects.create_user(username=request.POST["username"], password=request.POST["password"], email=request.POST["email"], is_developer=dev)

        return render(request, "register_success.html")
    return render(request, "index.html")

def login_view(request):
    if request.method == "POST":
        user = authenticate(username=request.POST["username"], password=request.POST["password"])

        if user is not None:
            login(request, user)
            return redirect("feed:dashboard")
        else:
            err = "Invalid Username/Password"
        
    else:
        err = None

    return render(request, "index.html", {"err":err})

def logout_view(request):
    logout(request)
    return redirect("users:index")