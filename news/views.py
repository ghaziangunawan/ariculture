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
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from news import models
from django.http import JsonResponse


def show_json(request):
    data = Feedback.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

# Create your views here.
@login_required(login_url='/account/login/')
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


@csrf_exempt
def save_review(request):
    if request.method == 'POST':
        var = User.objects.get(pk=request.user.id)
        name = request.POST.get("name")
        review = request.POST.get("review")
        date = request.POST.get("date")
        
        models.Feedback.objects.create(
            user=var,
            name=name,
            review=review,
            date = date
        )
        return JsonResponse({
              "status": True,
              "message": "Successfully Registered!"
                }, status=200)
    else:
         return JsonResponse({
              "status": False,
              "message": "Failed to Register."
            }, status=401)
