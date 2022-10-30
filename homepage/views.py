from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from homepage.models import Advertisement


def index(request):
    return render(request, 'index.html')

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account successfully created!')
            return redirect('homepage:login')
    
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
    response = HttpResponseRedirect(reverse('homepage:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/homepage/login/')
def show_advertisement_user(request):
    advertisement_item = Advertisement.objects.filter(user=request.user)
    context = {"list_item": advertisement_item, "username": str(request.user).upper(),"user_id" : request.user.id}   
    return render(request, 'advertisement_user.html',context)

@login_required(login_url='/homepage/login/')
def create_ad(request):
    if request.method == 'POST':
        response = HttpResponseRedirect(reverse('homepage:advertise'))
        Advertisement.objects.create(user = request.user,date = datetime.datetime.now(),title = request.POST.get('title'),description = request.POST.get('description'))
        return response
    context = {"username": str(request.user).upper()}
    return render(request, 'CreateAdvertising.html',context)

@login_required(login_url="/homepage/login/")
def set_remove(request, id):
    item = Advertisement.objects.get(user=request.user, id=id)
    item.delete()
    return HttpResponseRedirect(reverse("homepage:advertise"))
