from django.urls import path
from .views import RequestAddView, RequestListView

urlpatterns = [
    path('demand/<int:product_market>/', RequestAddView.as_view(), name='add_request'),
    path('demand/', RequestListView.as_view(), name='list_request'),
]
