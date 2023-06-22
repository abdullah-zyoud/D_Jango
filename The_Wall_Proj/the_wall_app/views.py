from django.shortcuts import render, HttpResponse,redirect
from .models import User ,Message,Comments
from django.contrib import messages
import bcrypt
from datetime import datetime, timezone


def index(request):
    return render(request, "index.html")

def register(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()  
        print(pw_hash)
        request.session['username'] = fname + " "+ lname
        request.session['status']="Registered"
        User.objects.create(first_name=fname, last_name=lname,email=email, password=pw_hash)
    return redirect("/")

def login(request):
    errors2 = User.objects.login_validator(request.POST)
    if len(errors2) > 0:
        for key, value in errors2.items():
            messages.error(request, value)
        return redirect('/')
   

    users = User.objects.filter(email=request.POST['email2'])
    if users:
        logged_user = users[0]
        if bcrypt.checkpw(request.POST['password2'].encode(), logged_user.password.encode()):
            request.session['username'] = logged_user.first_name
            request.session['user_id'] = logged_user.id
            

            request.session['status']="logged in"
            return redirect('/success')
        print("""Wrong password""")
    return redirect("/")

def add_message(request):
        user=User.objects.get(id= request.session['user_id'])
        new_message = Message.objects.create(message=request.POST['message'],user_id=user) 
       
        new_message.save()
        return redirect('/success')

def add_comment(request,message_id):
        user=User.objects.get(id= request.session['user_id'])
        message=Message.objects.get(id= message_id)

        new_comment = Comments.objects.create(comment=request.POST['comment'],user_id=user,message_id=message) 
       
        new_comment.save()
        return redirect('/success')

def success(request):
    # request.session['error']=""
    
    context={
        'user':User.objects.get(id=request.session["user_id"]),

        'messages':Message.objects.all(),
        'comments':Comments.objects.all(),
        'error' : request.session["error"]
    }
    return render(request,"success.html",context)

def logout(request):
    
    del request.session['user_id']
    del request.session['error']

    return redirect('/')

def delete(request,id):
     delete_message=Message.objects.get(id=id)
     current=datetime.now(timezone.utc)
     dif=current-delete_message.create_at
     if dif.total_seconds() <= 1800:
            request.session['error'] = ""
            delete_message.delete()
     else : 
          request.session['error']= " You cannot delete the message after 30 minutes"
     return redirect('/success')
