from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),	
    path('dojo_info', views.dojo_info),   
    path('ninja_info', views.ninja_info),   
    path('<int:id>', views.remove), 


   

]