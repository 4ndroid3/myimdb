""" Peliculas URL's """

from django.urls import include, path
from rest_framework import routers
from api.peliculas.views import PeliculaView, PersonasPeliculaView

router = routers.SimpleRouter()
router.register(r'', PeliculaView)
router.register(r'^(?P<slug>[^/.]+)/personas', PersonasPeliculaView)

urlpatterns = [
   path('', include(router.urls)),
]
