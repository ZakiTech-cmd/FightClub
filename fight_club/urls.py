from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter

from fighters.views import FighterViewSet
from titles.views import TitleViewSet

router = SimpleRouter()
router.register('titles', TitleViewSet)
router.register('fighters', FighterViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('matches/', include('matches.urls')),
    path('users/', include('users.urls')),
] + router.urls
