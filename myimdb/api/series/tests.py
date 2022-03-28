from random import randint, uniform
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from faker import Faker

from Rodajes.models import Serie


class SeriesTests(APITestCase):
    fake = Faker('es_ES')
    
    def test_create_serie(self):
        """
        Asegura que puedo crear una serie.
        """
        url = reverse('series-list')
        data = {
            "nombre": self.fake.name()
        }
        response = self.client.post(url, data, format='json')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Serie.objects.count(), 1)
    
    # def test_create_capitulo(self):
    #     """
    #     asegura que puedo crear un capitulo para una serie.
    #     """
    #     url = reverse('capitulos-list')
    #     data = {
    #         "nombre": self.fake.name(),
    #         "numero": randint(1, 10),
    #         "duracion": randint(20, 65),
    #         "puntuacion": round(uniform(0, 10), 2)
    #     }
    #     response = self.client.post(url, data, format='json')
    #     print(response.data)
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     self.assertEqual(Serie.objects.count(), 1)