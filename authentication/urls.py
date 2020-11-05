from django.urls import path
from django.contrib.auth.views import LoginView, logout_then_login
from .views import UserCreateView

urlpatterns = [
    path('signup/', UserCreateView.as_view(), name='user-create'),
    
    path('login/', LoginView.as_view(template_name='authentication/login.html', redirect_authenticated_user=True), name='login'),
    path('logout/', logout_then_login, name='logout'),
]
