from django.urls import path
from . import views	# the . indicates that the views file can be found in the same directory as this file
                    
urlpatterns = [
    path('', views.root),
    path('register', views.index),
    path('login', views.new),
    path('users/new', views.create),
    path('users', views.user),
]