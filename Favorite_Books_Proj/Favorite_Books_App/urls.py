from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('success', views.success),
    path('logout', views.logout),
    path('add_message', views.add_message),
    path('edit_book/<int:book_id>', views.edit_book),
    path('update/<int:id>', views.update_book),
    path('view_update/<int:id>', views.view_update),
    path('delete_book/<int:id>', views.delete_book),
    path('book/<int:id>/fav', views.add_favorit),
    path('book/<int:id>/unfav', views.remove_favorit),

]