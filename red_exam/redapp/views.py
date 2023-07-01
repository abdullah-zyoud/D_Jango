from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib import messages

def index(request): 
    return render(request, 'index.html')

def register(request):
    errors = User.objects.regValidator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        User.objects.create(username=request.POST['username'], email=request.POST['email'], password=request.POST['password'])
        return redirect ('/')

def login(request):
    errors = User.objects.loginValidator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
       
        this_user = User.objects.get(email=request.POST['email2'])
        request.session['user_id'] = this_user.id
        request.session['username']=this_user.username
        return redirect ('/display') 

def display(request): 
    context = {
        'username' : request.session['username'],
        'teams': Team.objects.all(),
       
    }

    return render(request, 'display.html', context) 

def logout(request): 
    request.session.flush()
    return redirect('/')

def dashborad(request): 
    return render(request, 'dashborad.html')

def create(request):
    return render(request, 'new.html')

def create_team(request):
    errors = Team.objects.create_team(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/create')
    else:
        Team.objects.create(
                    team_name = request.POST['team_name'], 
                    skill_level = request.POST['skill_level'], 
                    game_day = request.POST['game_day'],
                    user = User.objects.get(id=request.session['user_id']), 
                )
    return redirect('/display')

def details(request, team_id):
    context = {
        'teams' : Team.objects.get(id = team_id),
         'user_id' : request.session['user_id'],
    }
    return render(request, 'details.html', context)

def delete(request, team_id):
    dell = Team.objects.get(id = team_id)
    dell.delete() 
    return redirect('/display')

def edit_show(request, team_id):
    context = {
        'teams' : Team.objects.get(id=team_id) 
    }
    return render(request,'delEdi.html',context)

def edit(request, team_id):
    errors = Team.objects.update_team(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/edit_show/{team_id}')
    else:
    
        selected = Team.objects.get(id=team_id)
        selected.team_name = request.POST['team_name']
        selected.skill_level = request.POST['skill_level']
        selected.game_day = request.POST['game_day']
        selected.save()
        print('hi')
    return redirect('/display')



    