from django.urls import path
from .views import BuyView, SellView, NewProductView, DeleteProductView

urlpatterns = [
    path('buy/', BuyView.as_view(), name='buy'),
    path('sell/', SellView.as_view(), name='sell'),
    path('new-product/', NewProductView.as_view(), name='new_product'),
    path('delete-product/<int:pk>/', DeleteProductView.as_view(), name='delete_product'),
]
