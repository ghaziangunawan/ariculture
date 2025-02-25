from django.shortcuts import render
from advertisement.models import Advertisement
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from advertisement.models import *
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@login_required(login_url='/account/login/')
def show_advertisement(request):
    advertisement_item = Advertisement.objects.all().values()
    context = {"list_item": advertisement_item, "username": str(request.user)}   
    return render(request, 'advertisements.html',context)


def show_json(request):
    data = Advertisement.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@login_required(login_url='/account/login/')
def show_advertisement_user(request):
    advertisement_item = Advertisement.objects.filter(user=request.user)
    context = {"list_item": advertisement_item, "username": str(request.user).upper(),"user_id" : request.user.id}   
    return render(request, 'Advertisement_user.html', context)

@login_required(login_url="/account/login/")
def set_remove(request, id):
    item = Advertisement.objects.get(user=request.user, id=id)
    item.delete()
    return HttpResponseRedirect(reverse("advertisement:advertise"))


def show_advertisement_json_per_user(request):
    data = Advertisement.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def create_ad(request):
    username = str(request.user)
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        ad_type = request.POST.get("ad_type")
        var = User.objects.get(pk=request.user.id)
        Ad = Advertisement.objects.create(
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

@csrf_exempt
def save_ad_f(request):
    if request.method == 'POST':
        var = User.objects.get(pk=request.user.id)
        title = request.POST.get("title")
        description = request.POST.get("description")
        ad_type = request.POST.get("ad_type")
        username = str(request.user)
        
        Advertisement.objects.create(
            user=var,
            title=title,
            description=description,
            ad_type = ad_type,
            username = username
        )
        return JsonResponse({
            "status": True,
            "message": "Successfully Registered!"
                }, status=200)
    return JsonResponse({
            "status": False,
            "message": "Failed to Register."
            }, status=401)

@csrf_exempt
def set_remove_flutter(request, id):
    item = Advertisement.objects.get(user=User.objects.get(pk=request.user.id), id=id)
    item.delete()
    return JsonResponse({
                "status": True,
                "message": "Successfully Registered!"
                }, status=200)