from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
import math
from django.http import HttpResponseRedirect
from django.urls import reverse 
from django.views.decorators.csrf import csrf_exempt
from farmland.models import UserLand

dictPlantSpace = {
    'PD': 0.04,
    'JG': 0.14,
    'KT': 0.06,
    'SK': 0.96,
    'UJ': 0.25,
    'KE': 0.15,
    'WO': 0.01,
    'BW': 0.04,
    'TM': 0.28,
    'PS': 9,
    'JR': 20,
}

dictRecFert = {
    'PD': {"U": 200, "S": 100, "K": 75},
    'JG': {"U": 350, "S": 200, "K": 100},
    'KT': {"U": 100, "S": 100, "K": 50},
    'SK': {"U": 200, "S": 50, "K": 75},
    'UJ': {"U": 150, "S": 100, "K": 100},
    'KE': {"U": 350, "S": 200, "K": 400},
    'WO': {"U": 100, "S": 100, "K": 30},
    'BW': {"U": 350, "S": 100, "K": 50},
    'TM': {"U": 250, "S": 300, "K": 300},
    'PS': {"U": 350, "S": 150, "K": 150},
    'JR': {"U": 200, "S": 150, "K": 75},
}

dictWeight = {
    'PD': 5.7,
    'JG': 6.4,
    'KT': 1.5,
    'SK': 20,
    'UJ': 12,
    'KE': 16,
    'WO': 20,
    'BW': 9.5,
    'TM': 25,
    'PS': 28,
    'JR': 27,
}

dictRateSell = {
    'PD': 4,
    'JG': 4.6,
    'KT': 8,
    'SK': 1.1,
    'UJ': 5,
    'KE': 15,
    'WO': 4,
    'BW': 25,
    'TM': 5,
    'PS': 1.5,
    'JR': 5,
}

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

def calculate(size, plant):
    plantSpace = dictPlantSpace[plant]
    amount_of_plants = math.floor(size/plantSpace)
    
    urea1_needed = dictRecFert[plant]['U']*(size/10000)
    SP36_needed = dictRecFert[plant]['S']*(size/10000)
    KCl_needed = dictRecFert[plant]['K']*(size/10000)

    weight = dictWeight[plant]
    expected_yield = math.ceil((size/10000) * (weight*1000))

    rate_sell = dictRateSell[plant]
    gross_income = math.ceil(expected_yield * rate_sell * 1000)

    net_income = math.ceil(gross_income - ((urea1_needed * 13000) + (SP36_needed * 15000) + (KCl_needed * 20000)))

    return (amount_of_plants, 
            urea1_needed, 
            SP36_needed, 
            KCl_needed,
            expected_yield, 
            gross_income, 
            net_income)

@csrf_exempt
def addland(request):
    size = int(request.POST.get('size'))
    plant = request.POST.get('plant')

    (amount_of_plants, amount_of_u_needed,
    amount_of_s_needed, amount_of_k_needed, 
    expected_yield, gross_income, 
    net_income) = calculate(size, plant)

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

    return JsonResponse({
        "status": True,
        "message": "Successfully Added!"
    }, status=200)