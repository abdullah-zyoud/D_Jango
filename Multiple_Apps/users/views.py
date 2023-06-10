from django.shortcuts import render, HttpResponse ,redirect 
from django.http import JsonResponse


def root(request):
    return redirect("/users")

def index(request):
    return HttpResponse("placeholder for users to create a new user record")

def new(request):
    return HttpResponse("placeholder for users to log in")
def create(request):
     return redirect("/register")


def user(request):
    return HttpResponse("placeholder to later display all the list of users")



