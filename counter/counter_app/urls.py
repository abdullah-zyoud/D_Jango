from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),	   
    path('destroy_session', views.reset),
    path('add', views.add_two),
    path('user', views.user_number),


]