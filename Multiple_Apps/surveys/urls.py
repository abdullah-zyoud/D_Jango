from django.urls import path
from . import views	# the . indicates that the views file can be found in the same directory as this file
                    
urlpatterns = [
    # path('', views.root),
    path('/', views.index),
    path('/new', views.new),
    
    
]