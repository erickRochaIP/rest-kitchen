from django.test import TestCase, Client
from django.urls import reverse
from rest_framework.test import APIRequestFactory
from .models import Receita
from .serializers import ReceitaSerializer

client = Client()


# Create your tests here.
class ReceitaTestCase(TestCase):

    def setUp(self):
        Receita.objects.create(nome="Bolo de banana", descricao="Uma delicia de bolo", id_chef=1)
        Receita.objects.create(nome="Bolo de cenoura", descricao="Uma outra delicia de bolo", id_chef=1)
        Receita.objects.create(nome="Bolo de batata", descricao="Uma delicia desconhecida pela comunidade", id_chef=2)

    def test_get_all_receitas(self):
        response = client.get(reverse("receita-list"))
        receitas = Receita.objects.all()
        serializer = ReceitaSerializer(receitas, many=True)
        self.assertEqual(response.data, serializer.data)