from django.shortcuts import render ,redirect
from .models import Course
from django.contrib import messages
from .models import Course ,Description




def index(request):
    context = {
        "all_the_course": Course.objects.all(),
        "all_the_description": Description.objects.all()
    }
    
    return render(request, "index.html",context)


def add_course(request):
        errors = Course.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        
        new_course = Course.objects.create(name=request.POST['name']) 
        new_desc = Description.objects.create(course=new_course,desc=request.POST['desc'])
        new_desc.save()

        return redirect('/')

def view_delete(request, id):
    context = {
        'course': Course.objects.get(id=id)
    }

    return render(request, "delete.html", context)


def delete_Course(request, id):
    selected_course = Course.objects.get(id=id)
    selected_course.delete()
    return redirect('/')
