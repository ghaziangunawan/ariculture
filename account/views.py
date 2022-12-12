import datetime
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from farmland.models import UserLand
from account.forms import *
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

def account(request):
    return redirect('homepage:index')

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        print(request.POST)
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account successfully created!')
            return redirect('account:login')
        
        else:
            messages.info(request, 'Something is wrong!')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # login first
            response = HttpResponseRedirect(reverse("homepage:index")) # create response
            response.set_cookie('last_login', str(datetime.datetime.now())) # create last_login cookie and add it to response
            return response
        else:
            messages.info(request, 'Wrong Username or Password!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('account:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/account/login/')
def profile(request):
    print(request.user)
    data = UserLand.objects.filter(user_farmer=request.user)
    context = {
        "land_item": data,
        "username": request.user
    }
    return render(request, "profile.html", context)

def show_profile_json(request):
    data = UserLand.objects.filter(user_farmer=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@login_required(login_url="/account/login/")
def remove_land(request, id):
    item = UserLand.objects.get(user_farmer=request.user, id=id)
    item.delete()
    return HttpResponseRedirect(reverse("account:profile"))

def show_json(request):
    data = User.objects.filter(is_active = True)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@csrf_exempt
def login_f(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            # Redirect to a success page.
            return JsonResponse({
              "status": True,
              "message": "Successfully Logged In!"
              # Insert any extra data if you want to pass data to Flutter
            }, status=200)
        else:
            return JsonResponse({
              "status": False,
              "message": "Failed to Login, Account Disabled."
            }, status=401)
    else:
        return JsonResponse({
          "status": False,
          "message": "Failed to Login, check your email/password."
        }, status=401)

@csrf_exempt
def register_f(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({
              "status": True,
              "message": "Successfully Registered!"
                # Insert any extra data if you want to pass data to Flutter
            }, status=200)
        else:
            return JsonResponse({
              "status": False,
              "message": "Failed to Register."
            }, status=401)

def profile_json(request, user):
    print(type(request.user))
    print(user)
    req = User.objects.filter(username = user)
    print(req)
    data = UserLand.objects.filter(user_farmer=req[0])
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@csrf_exempt
def logout_user_f(request):
    logout(request)
    return JsonResponse({
              "status": True,
              "message": "Successfully Logout!"
                # Insert any extra data if you want to pass data to Flutter
        }, status=200)
