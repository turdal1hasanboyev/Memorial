from django.urls import path
from .api.SubEmail.SubEmailLC.views import SubEmailLCAPIView
from .api.SubEmail.SubEmailRUD.views import SubEmailRUDAPIView
from .api.Genre.GenreLC.views import GenreLCAPIView
from .api.Genre.GenreRUD.views import GenreRUDAPIView


urlpatterns = [
    path('sub_email_lc/', SubEmailLCAPIView.as_view(), name='sub-email-lc'),
    path('sub_email_rud/<int:pk>/', SubEmailRUDAPIView.as_view(), name='sub-email-rud'),
    path('genre_lc/', GenreLCAPIView.as_view(), name='genre-lc'),
    path('genre_rud/<int:pk>/', GenreRUDAPIView.as_view(), name='genre-rud'),
]