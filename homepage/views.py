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
def save_comment_f(request):
    if request.method == 'POST':
        var = User.objects.get(pk=request.user.id)
        name = request.POST.get("name")
        comment = request.POST.get("comment")
        
        
        models.Comments.objects.create(
            user=var,
            name=name,
            comment=comment,
        )
        return JsonResponse({
            "status": True,
            "message": "Successfully Commented!"
            }, status=200)
    else:
        return JsonResponse({
            "status": False,
            "message": "Failed to Comment."
            }, status=401)