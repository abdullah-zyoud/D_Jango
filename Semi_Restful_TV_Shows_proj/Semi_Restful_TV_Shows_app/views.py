from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Show


def index(request):
    context = {
        "all_the_shows": Show.objects.all()
    }
    return render(request, "all_show.html", context)


def add_Show(request):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/view_create_show')
    else:
        new_Show = Show.objects.create(title=request.POST['title'], network=request.POST['network'],
                                    release_date=request.POST['release_date'], description=request.POST['description'])
        new_Show.save()
        return redirect(f'view_show/{new_Show.id}')


def view_create_show(request):

    return render(request, "add_show.html")


def view_show(request, id):
    show = Show.objects.get(id=id)
    
    context = {
        'show': show,
       
    }
    return render(request, 'show.html', context)


def delete_Show(request, id):
    selected_show = Show.objects.get(id=id)
    selected_show.delete()
    return redirect('/')


def view_edit(request, id):
    context = {
        'show': Show.objects.get(id=id)
    }

    return render(request, "edit_show.html", context)


def edit_Show(request, id):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/view_create_show')
    selected_show = Show.objects.get(id=id)
    selected_show.title = request.POST['title']
    selected_show.network = request.POST['network']
    selected_show.release_date = request.POST['release_date']
    selected_show.description = request.POST['description']
    selected_show.save()
    return redirect(f'/view_show/{selected_show.id}')