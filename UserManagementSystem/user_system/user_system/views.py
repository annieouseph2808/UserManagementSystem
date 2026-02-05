from django.shortcuts import render, redirect
from .models import User
from .utils import check_password, hash_password
from django.contrib import messages

def accesslogin(request):
    return render(request, 'accesslogin.html')

def set_role(request):
    if request.method == "POST":
        request.session["login_role"] = request.POST.get("role")
        return redirect("login")

def login(request):
    role_selected = request.session.get("login_role")    
    
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
        return redirect(
            "adminscreen" if user.role == "superadmin" else "userscreen")
        
    return render(request, "login.html", {"role": role_selected})

def view_users(request):
    users = User.objects.all()
    return render(request, "user_list.html",{"users":users})

def user_details(request):
    email = request.GET.get("email")
    user = User.objects.get(email=email)
    return render(request, "user_detail.html", {"user": user})

def add_user(request):
    if request.method == "POST":
        User.objects.create(email=request.POST["email"],
            password=hash_password(request.POST["password"]),
            role=request.POST["role"])
        return redirect("view_users")

def remove_user(request):
    if request.method == "POST":
        User.objects.filter(email=request.POST["email"]).delete()
        return redirect("view_users")
    
def logout(request):
    request.session.flush()  
    return redirect("login")

def adminscreen(request):
    if request.session.get("role") != "superadmin":
        return redirect("login")
    return render(request,'admin.html')
def userscreen(request):
    return render(request,'user.html')
