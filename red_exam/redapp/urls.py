
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('display', views.display), 
    path('logout', views.logout),
    path ('dashborad', views.dashborad), 
    path('create', views.create),
    path('create_team', views.create_team),
    path('details/<team_id>', views.details),
    path('delete/<team_id>', views.delete),
    path('edit_show/<team_id>', views.edit_show),
    path('edit/<team_id>', views.edit)
]