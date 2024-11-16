from django.urls import path
from .api.SubEmail.SubEmailLC.views import SubEmailLCAPIView
from .api.SubEmail.SubEmailRUD.views import SubEmailRUDAPIView
from .api.Genre.GenreLC.views import GenreLCAPIView
from .api.Genre.GenreRUD.views import GenreRUDAPIView
from .api.CustomUser.CustomUserLC.views import CustomUserLCAPIView
from .api.CustomUser.CustomUserRUD.views import CustomUserRUDAPIView
from .api.Contact.ContactLC.views import ContactLCAPIView
from .api.Contact.ContactRUD.views import ContactRUDAPIView
from .api.Category.CategoryLC.views import CategoryLCAPIView
from .api.Category.CategoryRUD.views import CategoryRUDAPIView
from.api.Tag.TagLC.views import TagLCAPIView
from .api.Tag.TagRUD.views import TagRUDAPIView


urlpatterns = [
    path('sub_email_lc/', SubEmailLCAPIView.as_view(), name='sub-email-lc'),
    path('sub_email_rud/<int:pk>/', SubEmailRUDAPIView.as_view(), name='sub-email-rud'),
    path('genre_lc/', GenreLCAPIView.as_view(), name='genre-lc'),
    path('genre_rud/<int:pk>/', GenreRUDAPIView.as_view(), name='genre-rud'),
    path('custom_user_lc/', CustomUserLCAPIView.as_view(), name='custom-user-lc'),
    path('custom_user_rud/<int:pk>/', CustomUserRUDAPIView.as_view(), name='custom-user-rud'),
    path('contact_lc/', ContactLCAPIView.as_view(), name='contact-lc'),
    path('contact_rud/<int:pk>/', ContactRUDAPIView.as_view(), name='contact-rud'),
    path('category_lc/', CategoryLCAPIView.as_view(), name='category-lc'),
    path('category_rud/<slug:slug>/', CategoryRUDAPIView.as_view(), name='category-rud'),
    path('tag_lc/', TagLCAPIView.as_view(), name='tag-lc'),
    path('tag_rud/<int:pk>/', TagRUDAPIView.as_view(), name='tag-rud'),
]