from django.shortcuts import render, HttpResponse,redirect
from .models import User , Book
from django.contrib import messages
import bcrypt

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
        errors3 = User.objects.add_book_validator(request.POST)
        if len(errors3) > 0:
            for key, value in errors3.items():
                messages.error(request, value)
            return redirect('/success')
        else:
            uploaded_by=User.objects.get(id= request.session['user_id'])
            new_book = Book.objects.create(title=request.POST['title'],desc=request.POST['desc'] ,uploaded_by=uploaded_by) 
        
            new_book.save()
        return redirect('/success')

def success(request):
   
    context={
        'username': request.session['username'],
        'user_id' : User.objects.get(id= request.session['user_id']),
        'status':request.session['status'],
        'books' : Book.objects.all(),
    }
    return render(request,"success.html",context)

def edit_book(request ,book_id):
    
    user_id =request.session.get('user_id')
    if user_id : 
       context={
        'user': User.objects.get(id=user_id),
         'username': request.session['username'],
        'books' : Book.objects.get(id=book_id),
    }
       
       return render(request, "edit.html",context)

    else : 
            return redirect('/logout')


def view_update(request, id):
    user_id =request.session.get('user_id')
    context = {

        'books': Book.objects.get(id=id),
        'user': User.objects.get(id=user_id),

    }

    return render(request, "edit.html", context)
def update_book(request, id):
        errors3 = User.objects.add_book_validator(request.POST)
        if len(errors3) > 0:
            for key, value in errors3.items():
                messages.error(request, value)
            return redirect('/success')
        else:
    
            selected_book = Book.objects.get(id=id)
            selected_book.title = request.POST['title']
            selected_book.desc = request.POST['desc']
            selected_book.save()
            return redirect(f'/view_update/{selected_book.id}')

def delete_book(request, id):
    selected_book = Book.objects.get(id=id)
    selected_book.delete()
    return redirect('/success')

def add_favorit(request,book_id):
    book=Book.objects.get(id=book_id)
    book.users_who_like.add(User.objects.get(id=request.session['user_id']))
    return redirect(f'/view_update/{book_id}')

def remove_favorit(request,book_id):
    book=Book.objects.get(id=book_id)
    book.users_who_like.remove(User.objects.get(id=request.session['user_id']))
    return redirect(f'/view_update/{book_id}')

def logout(request):
    del request.session['username']
    del request.session['status']
    return redirect('/')
