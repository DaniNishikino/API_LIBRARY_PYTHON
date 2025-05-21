from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.BookNoParameters.as_view(), name='book_no_parameters'),
    path('book/<int:id>', views.BookWithParameters.as_view(), name='book_with_parameters'),
    path('author/', views.AuthorNoParameters.as_view(), name='author_no_parameters'),
    path('author/<int:id>', views.AuthorWithParameters.as_view(), name='author_with_parameters')
]