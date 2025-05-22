from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenObtainPairView
)

urlpatterns = [
    path('book/', views.BookNoParameters.as_view(), name='book_no_parameters'),
    path('book/<int:id>', views.BookWithParameters.as_view(), name='book_with_parameters'),
    path('author/', views.AuthorNoParameters.as_view(), name='author_no_parameters'),
    path('author/<int:id>', views.AuthorWithParameters.as_view(), name='author_with_parameters'),
    path('signup/', views.UserCreateView.as_view(), name='signup'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]