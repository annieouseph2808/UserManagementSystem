from django.shortcuts import render, redirect
from .models import User
from .utils import check_password
from django.contrib import messages

def accesslogin(request):
    return render(request, 'accesslogin.html')

def login(request):
    role = request.GET.get("role")
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            user = User.objects.get(email = email, is_active = True)
        except User.DoesNotExist:
            messages.error(request, "Invalid email")
            return redirect("login")
        role_selected = request.POST.get("role")

        if not check_password(password,user.password):
            messages.error(request,"Invalid password")
            return redirect("login")
        if user.role != role_selected:
            messages.error(request,"Unauthorized User")
            return redirect("login")
        
        request.session["user_id"] = user.id
        request.session["role"] = user.role

        if user.role == "superadmin":
            return redirect("adminscreen")
        else:
            return redirect("userscreen")
    return render(request, "login.html", {"role": role})


def adminscreen(request):
    return render(request,'admin.html')
def userscreen(request):
    return render(request,'user.html')
