from django.shortcuts import render, HttpResponse,redirect
import random

def index(request):

    
    number = random.randint(1, 100)
  
    if 'number' not in request.session:
        request.session['number'] = number
    
    context ={
        'number' : request.session['number'],
       
    }

    return render(request,'index.html',context)


def guess(request):
    num=request.POST['guess']
    request.session['guess'] = int(num)
    print(">>>>>>>>>>>>>>>>>>>")
    print(num)
    if 'attempts' not in request.session:
        request.session['attempts'] = 0
    request.session['attempts'] = int(request.session['attempts']) + 1

    return redirect('/')

def restart(request):
    del request.session['guess']
    del request.session['attempts']
    del request.session['number']

    return redirect('/')
