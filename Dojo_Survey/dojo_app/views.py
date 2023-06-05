from django.shortcuts import render 

# Create your views here.
def index(request):
    return render(request,"index.html")   


def create_user(request):
    print("Got Post Info....................")
    name_from_form = request.POST['name']
    Location_from_form = request.POST['Location']
    Language_from_form=request.POST['Language']
    Comment_from_form=request.POST['Comment']
    context = {
    	"name_on_template" : name_from_form,
    	"location_on_template" : Location_from_form,
        "Language_on_template" : Language_from_form,
         "Comment_on_template" : Comment_from_form,

    }
    return render(request,"index2.html",context)
