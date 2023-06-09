from django.shortcuts import render, HttpResponse,redirect
import  random

from datetime import datetime

def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
        request.session['move'] = 0
        request.session['end_game'] = False
    if 'activities' not in request.session:
        request.session['activities'] = []
        request.session['activities'].insert(0,"Game Begin")

    context ={
        'gold' : request.session['gold'],
        'move' : request.session['move'],
        'end_game' : request.session['end_game'],
        'activities' : request.session['activities'],
    }
    return render(request,'index.html',context)

def process_money(request):
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if request.session['end_game']: 
        return redirect('/')
    if request.session['move'] > 14 and not request.session['end_game']:
        if request.session['gold'] >= 100:
            request.session['activities'].insert(1, f"You won! ({now}) - Reset to play again!")
        else:
            request.session['activities'].insert(1, f"You lost.. ({now}) - Reset to play again..")
        request.session['end_game'] = True
        return redirect('/')

    if request.POST['action'] == "casino":
        gold = random.randint(0, 50)
        if random.randint(1, 4)%2 == 1:
            request.session['gold'] -= gold
            request.session['activities'].insert(1, f"Entered a casino and lost {gold} golds.. Ouch.. ({now})")
        else:
            request.session['gold'] += gold
            request.session['activities'].insert(1, f"Entered a casino and earned {gold} golds! Yeah! ({now})")
    else:
        if request.POST['action'] == "farm":
            gold = random.randint(10, 20)
        if request.POST['action'] == "cave":
            gold = random.randint(5, 10)
        if request.POST['action'] == "house":
            gold = random.randint(2, 5)
        request.session['gold'] += gold
        request.session['activities'].insert(1, f"Earned {gold} golds from the {request.POST['action']}! ({now})")
    request.session['move'] += 1
    return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')