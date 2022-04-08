""" Series URL's """

from django.urls import include, path
from rest_framework import routers
from api.series.views import CapituloView, PersonasSerieView, SeriesView, TemporadaView

router = routers.SimpleRouter()
router.register(r'', SeriesView)
router.register(r'^(?P<slug>[^/.]+)/temporadas', TemporadaView)
router.register(r'^(?P<slug>[^/.]+)/capitulos', CapituloView)
router.register(r'^(?P<slug>[^/.]+)/personas', PersonasSerieView)

app_name = 'series-api'
urlpatterns = [
   path('', include(router.urls)),
]
