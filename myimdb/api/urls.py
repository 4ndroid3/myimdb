from django.urls import include, path
from api.peliculas import urls as peliculas_url
from api.series import urls as series_url


urlpatterns = [
    path(
      'peliculas/',
      include(peliculas_url),
      name='api_peliculas'
   ),
   path(
      'series/',
      include(series_url),
      name='api_series'
   ),
]