from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from . import models
from django.core import serializers
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect,HttpResponseNotFound
from . import forms
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return render(request, 'index.html')

@login_required(login_url='/account/login/')
def show_advertisement_user(request):
    advertisement_item = models.Advertisement.objects.filter(user=request.user)
    context = {"list_item": advertisement_item, "username": str(request.user).upper(),"user_id" : request.user.id}   
    return render(request, 'Advertisement_user.html', context)

@login_required(login_url="/account/login/")
def set_remove(request, id):
    item = models.Advertisement.objects.get(user=request.user, id=id)
    item.delete()
    return HttpResponseRedirect(reverse("homepage:advertise"))


def show_json(request):
    data = models.Advertisement.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def create_ad(request):
    username = str(request.user)
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        ad_type = request.POST.get("ad_type")
        var = User.objects.get(pk=request.user.id)
        Ad = models.Advertisement.objects.create(
            user=var,
            title=title,
            description=description,
            ad_type = ad_type,
            username = username
        )
        return JsonResponse(
            {
                "pk": Ad.id,
                "fields": {
                    "user" : Ad.user.username,
                    "title": Ad.title,
                    "description": Ad.description,
                    "ad_type" : Ad.ad_type,
                    "date": Ad.date,
                    "username" : Ad.username
                },
            },
            status=200,
        )

def show_comment(request):
    comment = models.Comments.objects.all()
    form = forms.CommentForm(request.POST)
    context = {
        'data_comment': comment,
        'form': form,
    }
    return render(request,"index.html", context)


def get_comment(request):
    comment = models.Comments.objects.all()
    data = serializers.serialize("json", comment)
    return HttpResponse(data, content_type="application/json")


def add_comment(request):
    form = forms.CommentForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.save()
            return show_comment(request)
        return HttpResponseNotFound()        
    return HttpResponseNotFound()

@csrf_exempt
def save_ad_f(request):
    if request.method == 'POST':
        var = User.objects.get(pk=request.user.id)
        title = request.POST.get("title")
        description = request.POST.get("description")
        ad_type = request.POST.get("ad_type")
        username = str(request.user)
        
        models.Advertisement.objects.create(
            user=var,
            title=title,
            description=description,
            ad_type = ad_type,
            username = username
        )
        return HttpResponse(b"CREATED", status=201)
    return HttpResponseNotFound()