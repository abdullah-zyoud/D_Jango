from django.shortcuts import render, HttpResponse
    
def another_method(request, my_val):
     return HttpResponse(f" {my_val}")	# my_val would be a number from the URL
    # given the example above, my_val would be 23
    
def yet_another(request, name):
      return HttpResponse("String response from root_method")	# name would be a string from the URL
    # given the example above, name would be 'pooh'
    
def one_more(request, id, color):
       return HttpResponse("String response from root_method") 	# id would be a number, and color a string from the URL
    # given the example above, id would be 17 and color would be 'brown'
