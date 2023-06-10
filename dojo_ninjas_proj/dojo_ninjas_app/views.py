from django.shortcuts import render ,redirect

from .models import Dojo ,Ninja

def index(request):
    context = {
    	"all_dojo": Dojo.objects.all(),
        "all_ninja": Ninja.objects.all()
    }
    return render(request, "index.html", context)

def dojo_info(request):
    if request.method =='POST':
        name=request.POST['name']
        city=request.POST['city']
        state=request.POST['state'] 
        new_dojo =Dojo(name=name,city=city,state=state)
        new_dojo.save()
    return redirect( "/")

def ninja_info(request):

    if request.method =='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        dojo=Dojo.objects.get(id=request.POST['dojo'])
        new_ninja =Ninja(first_name=first_name,last_name=last_name,dojo=dojo)
        new_ninja.save()
    return redirect( "/")

def remove (request,id):
    dojo=Dojo.objects.get(id=id)
    dojo.delete()
    return redirect('/')

