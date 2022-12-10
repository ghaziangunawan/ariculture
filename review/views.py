import json
from django.shortcuts import render
from review.models import Review
from django.http import HttpResponse, HttpResponseNotFound
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

# Create your views here.
# utk nunjukin html nya
def show_review(request):
    user_map = {}
    for us in get_user_model().objects.all():
        user_map[str(us.id)] = us.username
    context = { "users": json.dumps(user_map) }
    return render(request, "review.html", context)

# buat mskin review baru ke database
def create_review(request):
    if request.method == 'POST':
        rating = request.POST.get('rating')
        review_text = request.POST.get('review_text')
        Review.objects.create(
            user = request.user,
            rating = rating,
            date = datetime.datetime.now(),
            review_text = review_text
        )
        return HttpResponse(b"CREATED", status=201)
    
    return HttpResponseNotFound()

# buat nge fetch data dari database ke bentuk json
def show_json(request):
    data = Review.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@csrf_exempt
def save_review(request):
    if request.method == 'POST':
        rating = request.POST.get('rating')
        review_text = request.POST.get('review_text')
        Review.objects.create(
            user = request.user,
            rating = rating,
            date = datetime.datetime.now(),
            review_text = review_text
        )
        return HttpResponse(b"CREATED", status=201)
    
    return HttpResponseNotFound()