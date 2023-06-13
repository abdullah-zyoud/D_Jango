from django.urls import path
from . import views
                    
urlpatterns = [
    
    path('', views.index),
    path('authors', views.author),
    path('books/<int:id>', views.books),
    path('aut/<int:id>', views.aut),
    path('books/<int:book_id>/add', views.add_author),
    path('aut/<int:author_id>/add', views.add_book),

   
    
]

