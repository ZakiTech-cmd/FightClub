from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter

from fight_club import settings
from fighters.views import FighterViewSet
from matches.views import MatchViewSet
from titles.views import TitleViewSet

router = SimpleRouter()
router.register('titles', TitleViewSet)
router.register('fighters', FighterViewSet)
router.register('matches', MatchViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
] + router.urls + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
