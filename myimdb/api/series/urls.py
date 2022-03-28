""" Series URL's """

from django.urls import include, path
# from rest_framework import routers
from rest_framework_nested import routers
from api.series.views import CapituloView, PersonasSerieView, SeriesView, TemporadaView

router = routers.SimpleRouter()
router.register(r'', SeriesView, basename='series')
temporadas_router = routers.NestedSimpleRouter(router, r'', lookup='series')
temporadas_router.register(r'temporadas', TemporadaView, basename='temporadas')
capitulos_router = routers.NestedSimpleRouter(temporadas_router, r'temporadas', lookup='temporadas')
capitulos_router.register(r'capitulos', CapituloView, basename='capitulos')
personas_router = routers.NestedSimpleRouter(router, r'', lookup='series')
personas_router.register(r'personas', PersonasSerieView, basename='personas')

urlpatterns = [
   path('', include(router.urls)),
   path('', include(capitulos_router.urls)),
   path('', include(temporadas_router.urls)),
   path('', include(personas_router.urls)),
]
