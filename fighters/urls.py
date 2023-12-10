# fighters/urls.py
from django.urls import path
from .views import FighterListCreateView, FighterRetrieveUpdateDestroyView, TitleListCreateView, \
    TitleRetrieveUpdateDestroyView, MatchListCreateView, MatchRetrieveUpdateDestroyView

urlpatterns = [
    path('fighters', FighterListCreateView.as_view(), name='fighter-list-create'),
    path('fighters/<int:pk>', FighterRetrieveUpdateDestroyView.as_view(), name='fighter-retrieve-update-destroy'),
    path('titles', TitleListCreateView.as_view(), name='title-list-create'),
    path('titles/<int:pk>', TitleRetrieveUpdateDestroyView.as_view(), name='title-retrieve-update-destroy'),
    path('matches', MatchListCreateView.as_view(), name='match-list-create'),
    path('matches/<int:pk>', MatchRetrieveUpdateDestroyView.as_view(), name='match-retrieve-update-destroy'),
]
