from rest_framework.authtoken.views import obtain_auth_token
from . import views
from django.urls import path
from .views import RegisterView, CustomObtainAuthToken, LogoutView

urlpatterns = [
    path('logout', LogoutView.as_view(), name='logout'),
    path('register', RegisterView.as_view(), name='register'),
    path('login', CustomObtainAuthToken.as_view(), name='login'),
]
