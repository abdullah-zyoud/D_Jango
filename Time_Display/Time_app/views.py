
from django.shortcuts import render 
from time import gmtime, strftime
from datetime import datetime
from django.http import HttpResponse
    
def index(request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
    }
    return render(request,'index.html', context)

def index2(request):
    current_time = datetime.now().strftime('%H:%M:%S')   
    html = "<html><body><b>Current Time Value:</b> %s</body></html>" % current_time
    return HttpResponse(html)