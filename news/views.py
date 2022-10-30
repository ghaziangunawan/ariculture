from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect,HttpResponseNotFound
from django.urls import reverse
from news.models import Feedback
from django.core import serializers
from news.forms import FeedbackForm



# Create your views here.
@login_required(login_url='/news/login/')
def show_news(request):
    feedbacks = Feedback.objects.all()
    form = FeedbackForm(request.POST)
    context = {
        'data_feedback': feedbacks,
        'form': form,
    }
    return render(request,"news.html", context)

@login_required(login_url='/account/login/')
def get_feedback(request):
    feedbacks = Feedback.objects.all()
    data = serializers.serialize("json", feedbacks)
    return HttpResponse(data, content_type="application/json")

@login_required(login_url='/account/login/')
def add_feedback(request):
    form = FeedbackForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user = request.user
            feedback.save()
            return show_news(request)
        return HttpResponseNotFound()        
    return HttpResponseNotFound()

@login_required(login_url='/account/login/')
def delete_task(request,id):
    task = Feedback.objects.filter(id =id)
    task.delete()
    return show_news(request)


def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account successfully created!')
            return redirect('account:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # login first
            response = HttpResponseRedirect(reverse("account:index")) # create response
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