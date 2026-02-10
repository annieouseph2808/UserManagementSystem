from django.shortcuts import redirect
from django.contrib import messages

def role_required(allowed_roles):
    def decorator(passed_func):
        def wrapper(request,*args, **kwargs):
            role = request.session.get("role")
            if role not in allowed_roles:
                messages.error(request,"Unathorized access")
                return redirect("login")
            return passed_func(request, *args, **kwargs)
        return wrapper
    return decorator