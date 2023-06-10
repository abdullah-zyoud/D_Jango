from django.urls import path
from . import views	# the . indicates that the views file can be found in the same directory as this file
                    
urlpatterns = [
    
    path('/', views.index),
    path('/new', views.new),
    path('/create', views.create),
    path('/<int:number>', views.show),
    path('/<int:number>/edit', views.edit),
    path('/<int:number>/delete', views.destroy),
    path('/json', views.printjson),

    
]

