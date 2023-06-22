from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('success', views.success),
    path('logout', views.logout),
    path('message', views.add_message),
    path('comment/<int:message_id>', views.add_comment),
    path('delete/<int:id>', views.delete),

]