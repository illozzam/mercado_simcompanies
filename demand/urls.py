from django.urls import path
from .views import RequestAddView, RequestListView, RequestMarkDoneView

urlpatterns = [
    path('demand/mark-done/<int:id_request>/', RequestMarkDoneView.as_view(), name='mark_done'),
    path('demand/add/<int:product_market>/', RequestAddView.as_view(), name='add_request'),
    path('demand/', RequestListView.as_view(), name='list_request'),
]
