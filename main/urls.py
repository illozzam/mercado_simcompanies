from django.urls import path
from .views import InitialView, PageView

urlpatterns = [
    path('', InitialView.as_view(), name='initial'),
    path('page/<slug:url>/', PageView.as_view(), name='page'),
]
