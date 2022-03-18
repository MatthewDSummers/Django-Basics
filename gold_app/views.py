from django.shortcuts import render, redirect
import random
from datetime import datetime

now = datetime.now()
date_time = now.strftime("%Y/%m/%d, %-I:%M %p")

def index(request):
    return render(request, 'index.html')

def process_money(request):
    if 'total_gold' not in request.session:
        request.session['total_gold'] = 0
        request.session['activities']=[]

    if request.POST['place'] == 'farm':
        r1 = random.randint(10, 20)
        request.session['activities'].append("You earned " + str(r1) + " gold!" + "          (" + str(date_time) + ")")
        request.session['total_gold'] += r1
        return redirect('/')

    elif request.POST['place'] == 'cave':
        r2 = random.randint(5,10)
        request.session['activities'].append("You earned " + str(r2) + " gold!" + "          (" + str(date_time) + ")")
        request.session['total_gold'] += r2
        return redirect('/')

    elif request.POST['place'] == 'house':
        r3 = random.randint(2, 5)
        request.session['activities'].append("You earned " + str(r3) + " gold!" + "          (" + str(date_time) + ")")
        request.session['total_gold'] += r3
        return redirect('/')

    elif request.POST['place'] == 'casino':
        r4 = random.randint(-50, 50)
        request.session['activities'].append("You earned " + str(r4) + " gold!" + "          (" + str(date_time) + ")")
        request.session['total_gold'] += r4
        return redirect('/')
