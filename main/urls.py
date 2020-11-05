from django.urls import path
from .views import InitialView

urlpatterns = [
    path('', InitialView.as_view(), name='initial'),
]
