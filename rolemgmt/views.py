from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login
from django.http import HttpResponseRedirect
from django.views.decorators.http import require_http_methods
from django.contrib.auth.models import User
from rmtmgmt.models import UserProfile
from rolemgmt.models import RoleConfig


@require_http_methods(['GET', 'POST'])
def user_login(request):
    """
    user authendication function.
    """
    title = "Log In"
    error = ""
    if request.method == 'POST':
        user = authenticate(username=request.POST.get('email'),
                            password=request.POST.get('password'))
        if user is not None:
            if user.is_active and user.is_staff:
                role_conf = RoleConfig.objects.filter(user=user).exists()
                if role_conf:
                    auth_login(request, user)
                    return HttpResponseRedirect("/resume-management/")
                else:
                    error = "Your Role is not defined. Please contact administrator."
            else:
                error = "Your Account is not activated. Please contact administrator."
        else:
            error = "Enter the valid details."
    return render(request, 'login.html', {'error': error, 'title': title, })


@require_http_methods(['GET', 'POST'])
def user_registration(request):
    """
    Registration function for onboard new user in RMT.
    """
    title = "Registration"
    if request.method == "POST":
        data = request.POST.copy()
        if data.get("first_name") and data.get("last_name") \
           and data.get("email") and data.get("mobile") \
           and data.get("password") and data.get("password_confirm"):
            email = data.get('email')
            user_email = User.objects.filter(username=email,
                                             email=email).exists()
            if user_email:
                error = "Email already exists."
            else:
                user = User.objects.create_user(
                    username=email,
                    password=data.get("password_confirm"),
                    email=email)
                user.first_name = data.get("first_name")
                user.last_name = data.get("last_name")
                user.is_active = False
                user.is_staff = False
                user.save()
                user_profile = UserProfile.objects.create(
                    user=user,
                    mobile=data.get("mobile"))
                return HttpResponseRedirect("/user-login/")
    return render(request, 'register.html', locals())
