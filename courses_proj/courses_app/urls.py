from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('create_course', views.add_course),
    path('view_delete/<int:id>', views.view_delete),
    path('delete_course/<int:id>', views.delete_Course),
   
]