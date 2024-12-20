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
from .api.Award.AwardLC.views import AwardLCAPIView
from .api.Award.AwardRUD.views import AwardRUDAPIView
from .api.About.AboutLC.views import AboutLCAPIView
from .api.About.AboutRUD.views import AboutRUDAPIView
from .api.Banner.BannerLC.views import BannerLCAPIView
from .api.Banner.BannerRUD.views import BannerRUDAPIView
from .api.Book.BookCreate.views import BookCreateAPIView
from .api.Book.BookDestroy.views import BookDestroyAPIView
from .api.Book.BookList.views import BookListAPIView
from .api.Book.BookRetrieve.views import BookRetrieveAPIView
from .api.Book.BookUpdate.views import BookUpdateAPIView
from .api.MyBook.MyBookCreate.views import MyBookCreateAPIView
from .api.MyBook.MyBookDestroy.views import MyBookDestroyAPIView
from .api.MyBook.MyBookUpdate.views import MyBookUpdateAPIView
from .api.MyBook.MyBookList.views import MyBookListAPIView
from .api.MyBook.MyBookRetrieve.views import MyBookRetrieveAPIView
from .api.Review.ReviewCreate.views import ReviewCreateAPIView
from .api.Review.ReviewDestroy.views import ReviewDestroyAPIView
from .api.Review.ReviewList.views import ReviewListAPIView
from .api.Review.ReviewUpdate.views import ReviewUpdateAPIView
from .api.Review.ReviewRetrieve.views import ReviewRetrieveAPIView


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
    path('award_lc/', AwardLCAPIView.as_view(), name='award-lc'),
    path('award_rud/<int:pk>/', AwardRUDAPIView.as_view(), name='award-rud'),
    path('about_lc/', AboutLCAPIView.as_view(), name='about_lc'),
    path('about_rud/<int:pk>/', AboutRUDAPIView.as_view(), name='about_rud'),
    path('banner_lc/', BannerLCAPIView.as_view(), name='banner_lc'),
    path('banner_rud/<int:pk>/', BannerRUDAPIView.as_view(), name='banner_rud'),
    path('book_create/', BookCreateAPIView.as_view(), name='book-create'),
    path('book_destroy/<slug:slug>/', BookDestroyAPIView.as_view(), name='book-destroy'),
    path('book_list/', BookListAPIView.as_view(), name='book-list'),
    path('book_retrieve/<slug:slug>/', BookRetrieveAPIView.as_view(), name='book-retrieve'),
    path('book_update/<slug:slug>/', BookUpdateAPIView.as_view(), name='book-update'),
    path('my_book_create/', MyBookCreateAPIView.as_view(), name='my-book-create'),
    path('my_book_destroy/<int:pk>/', MyBookDestroyAPIView.as_view(), name='my-book-destroy'),
    path('my_book_update/<int:pk>/', MyBookUpdateAPIView.as_view(), name='my-book-update'),
    path('my_book_list/', MyBookListAPIView.as_view(), name='my-book-list'),
    path('my_book_retrieve/<int:pk>/', MyBookRetrieveAPIView.as_view(), name='my-book-retrieve'),
    path('review_create/', ReviewCreateAPIView.as_view(), name='review-create'),
    path('review_destroy/<int:pk>/', ReviewDestroyAPIView.as_view(), name='review-destroy'),
    path('review_list/', ReviewListAPIView.as_view(), name='review-list'),
    path('review_update/<int:pk>/', ReviewUpdateAPIView.as_view(), name='review-update'),
    path('review_retrieve/<int:pk>/', ReviewRetrieveAPIView.as_view(), name='review-retrieve'),
]