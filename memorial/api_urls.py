from django.urls import path
from .api.SubEmail.SubEmailLC.views import SubEmailLCAPIView
from .api.SubEmail.SubEmailRUD.views import SubEmailRUDAPIView


urlpatterns = [
    path('sub_email_lc/', SubEmailLCAPIView.as_view(), name='sub-email-lc'),
    path('sub_email_rud/<int:pk>/', SubEmailRUDAPIView.as_view(), name='sub-email-rud'),
]