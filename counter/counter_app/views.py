from django.shortcuts import render, HttpResponse,redirect


def index(request):
    if request.method == "POST" and 'count'  in request.POST :
      try:
         request.session['count'] +=1

      except:
         request.session['count'] = 0
      
    
    return render(request,'index.html')

def reset(request):
    del request.session['count']
    return redirect('/')

def add_two(request):
    request.session['count'] += 2
    return redirect('/')

def user_number(request):
    request.session['number'] = request.POST['number']
    request.session['count'] += int(request.session['number'])
   
    return redirect('/')