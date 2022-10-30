from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse 
from farmland.models import UserLand

# Create your views here.
@login_required(login_url="account:login")
def show_farmland(request):
    return render(request, "farmland.html", {})

def create_userland(request):
    if request.method == 'POST':
        size = request.POST.get('size')
        plant = request.POST.get('plant')
        amount_of_plants = request.POST.get('amount_of_plants')
        amount_of_u_needed = request.POST.get('amount_of_u_needed')
        amount_of_s_needed = request.POST.get('amount_of_s_needed')
        amount_of_k_needed = request.POST.get('amount_of_k_needed')
        expected_yield = request.POST.get('expected_yield')
        gross_income = request.POST.get('gross_income')
        net_income = request.POST.get('net_income')

        UserLand.objects.create(
            user_farmer = request.user,
            size = size,
            plant = plant,
            amount_of_plants = amount_of_plants,
            amount_of_u_needed = amount_of_u_needed,
            amount_of_s_needed = amount_of_s_needed,
            amount_of_k_needed = amount_of_k_needed,
            expected_yield = expected_yield,
            gross_income = gross_income,
            net_income = net_income
        )
        return HttpResponse(b"CREATED", status=201)
    
    return HttpResponseNotFound()