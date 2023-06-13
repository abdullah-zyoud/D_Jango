from django.shortcuts import render ,redirect

from .models import Book ,Author

def index(request):
    if request.method =='POST':
        title=request.POST['title']
        desc=request.POST['desc']
        new_book =Book(title=title,desc=desc)
        new_book.save()
    context = {
    	"all_the_book": Book.objects.all(),
        
    }
    
    return render(request, "index1.html",context)

def author(request):
    if request.method =='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        notes=request.POST['notes']
        new_author=Author(first_name=first_name,last_name=last_name,notes=notes)
        new_author.save()
    context = {
    	
        "all_the_author": Author.objects.all(),
    }
    
    return render(request, "index2.html",context)

def books(request,id):
    
    context = {
    	
       'book':Book.objects.get(id=id),
       
       "all_the_author": Author.objects.exclude(books__id=id),
    }
    
    return render(request, "index3.html",context)

def aut(request,id):
    context = {
    	
       'author':Author.objects.get(id=id),
       "all_the_book": Book.objects.exclude(authors__id=id),

       
    }
    
    return render(request, "index4.html",context)

def add_author(request,book_id):
    book=Book.objects.get(id=book_id)
    author=Author.objects.get(id=request.POST['book_select'])
    book.authors.add(author)
    return redirect(f'/books/{book_id}')


def add_book(request,author_id):
    book = Book.objects.get(id=request.POST['author_select'])
    author = Author.objects.get(id=author_id)
    book.authors.add(author)
    return redirect(f'/aut/{author_id}')

