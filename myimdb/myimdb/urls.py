""" Archivo pricipal de URL's """

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib import admin
from django.urls import include, path, re_path
from api import urls as api_urls

SchemaView = get_schema_view(
   openapi.Info(
      title="My Own IMDB API",
      default_version='v0.1',
      description="API para registrar peliculas, series y los actores/directores que participan en las mismas",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="asj@gmail.com"),
      license=openapi.License(name="Sin licencia"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)
urlpatterns = [
    re_path(
       r'^swagger(?P<format>\.json|\.yaml)$',
       SchemaView.without_ui(cache_timeout=0),
       name='schema-json'
   ),
   re_path(
      r'^swagger/$',
      SchemaView.with_ui('swagger', cache_timeout=0),
      name='schema-swagger-ui'
   ),
   re_path(
      r'^redoc/$',
      SchemaView.with_ui('redoc', cache_timeout=0),
      name='schema-redoc'
   ),
   path(
      'api/',
      include(api_urls),
      name='api'
   ),
   
   path(
      'admin/',
      admin.site.urls
   ),
]
