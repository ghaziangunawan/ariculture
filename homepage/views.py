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
from homepage.models import Advertisement
from django.core import serializers
from django.contrib.auth.models import User


def index(request):
    return render(request, 'index.html')

@login_required(login_url='/account/login/')
def show_advertisement_user(request):
    advertisement_item = Advertisement.objects.filter(user=request.user)
    context = {"list_item": advertisement_item, "username": str(request.user).upper(),"user_id" : request.user.id}   
    return render(request, 'advertisement_user.html',context)

@login_required(login_url="/account/login/")
def set_remove(request, id):
    item = Advertisement.objects.get(user=request.user, id=id)
    item.delete()
    return HttpResponseRedirect(reverse("homepage:advertise"))

@login_required(login_url="/account/login/")
def show_json(request):
    data = Advertisement.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def create_ad(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        ad_type = request.POST.get("ad_type")
        var = User.objects.get(pk=request.user.id)

        Ad = Advertisement.objects.create(
            user=var,
            title=title,
            description=description,
            ad_type = ad_type
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
                },
            },
            status=200,
        )

