""" Peliculas URL's """

from django.urls import include, path
from rest_framework_nested import routers
from api.peliculas.views import PeliculaView, PersonasPeliculaView

router = routers.SimpleRouter()
router.register(r'', PeliculaView, basename='peliculas')
personas_router = routers.NestedSimpleRouter(router, r'', lookup='peliculas')
personas_router.register(r'personas', PersonasPeliculaView, basename='personas')

urlpatterns = [
   path('', include(router.urls)),
   path('', include(personas_router.urls)),
]
