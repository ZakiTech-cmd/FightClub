from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from .views import RegisterView, LogoutView, UserDetailView

urlpatterns = [
    path('logout', LogoutView.as_view(), name='logout'),
    path('register', RegisterView.as_view(), name='register'),
    path('login', obtain_auth_token, name='login'),
    path('my-profile/', UserDetailView.as_view(), name='my-profile'),
]
