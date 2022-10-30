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

def account(request):
    return redirect('homepage:index')

def register(request):
    form = UserForm()

    if request.method == "POST":
        form = UserForm(request.POST)
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
    data = UserLand.objects.filter(user_farmer=request.user)
    context = {
        "land_item": data,
        "first_name": str(request.user.first_name)
    }
    return render(request, "profile.html", context)

@login_required(login_url="/account/login/")
def remove_land(request, id):
    item = UserLand.objects.get(user_farmer=request.user, id=id)
    item.delete()
    return HttpResponseRedirect(reverse("account:profile"))
