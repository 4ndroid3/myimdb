from random import randint, uniform
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from faker import Faker

from Rodajes.models import Pelicula


class PeliculasTests(APITestCase):
    fake = Faker('es_ES')
    
    def test_create_pelicula(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('peliculas-list')
        data = {
            "nombre": self.fake.name(),
            "duracion": randint(90, 180),
            "puntuacion": round(uniform(0, 10), 2),
        }
        response = self.client.post(url, data, format='json')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Pelicula.objects.count(), 1)