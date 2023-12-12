# fighters/urls.py
from django.urls import path
from .views import FighterListCreateView, FighterRetrieveUpdateDestroyView

urlpatterns = [
    path('', FighterListCreateView.as_view(), name='fighter-list-create'),
    path('<int:pk>', FighterRetrieveUpdateDestroyView.as_view(), name='fighter-retrieve-update-destroy')
]
