from django.urls import path
from .views import home_page_view, books_page_view, about_page_view, book_detail_page_view, library_page_view, contact_page_view, register_page_view, login_page_view, logout_view


urlpatterns = [
    path('', home_page_view, name='home'),
    path('books/', books_page_view, name='books'),
    path('about/', about_page_view, name='about'),
    path('book-single/<slug:slug>/', book_detail_page_view, name='book-single'),
    path('library/', library_page_view, name='library'),
    path('contact/', contact_page_view, name='contact'),
    path('register/', register_page_view, name='register'),
    path('login/', login_page_view, name='login'),
    path('logout/', logout_view, name='logout'),
]