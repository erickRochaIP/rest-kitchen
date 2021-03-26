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
        Receita.objects.create(nome="Bolo de batata", descricao="Uma delicia desconhecida pelas pessoas", id_chef=2)
        Receita.objects.create(nome="Pãozinho", descricao="Um pequeno pão", id_chef=2)
        Receita.objects.create(nome="Pão de batata", descricao="Ótimo para despertar boas lembranças")
        Receita.objects.create(nome="Macarrão", descricao="Prato internacional", id_chef=3)
        Receita.objects.create(nome="Mistério", descricao="Um mistério culinário")

    def test_get_all_receitas(self):
        response = client.get(reverse("receita-list"))
        receitas = Receita.objects.all()
        serializer = ReceitaSerializer(receitas, many=True)
        self.assertEqual(response.data, serializer.data)

    def test_get_receitas_by_id_chef(self):
        response = client.get(reverse("receita-list"), {'id_chef': 1})
        receitas = Receita.objects.filter(id_chef=1)
        serializer = ReceitaSerializer(receitas, many=True)
        self.assertEqual(response.data, serializer.data)

    def test_get_receitas_by_nome(self):
        response = client.get(reverse("receita-list"), {'nome': "Pão"})
        receitas = Receita.objects.filter(nome__contains="Pão")
        serializer = ReceitaSerializer(receitas, many=True)
        self.assertEqual(response.data, serializer.data)

    def test_get_receitas_by_nome_and_descricao(self):
        response = client.get(reverse("receita-list"), {'nome': "Bolo", 'descricao': 'bolo'})
        receitas = Receita.objects.filter(nome__contains="Bolo").filter(descricao__contains="bolo")
        serializer = ReceitaSerializer(receitas, many=True)
        self.assertEqual(response.data, serializer.data)

    def test_post_wrong_receita(self):
        response = client.post(reverse("receita-list"), {'nome': 'Bolinho'})
        self.assertEqual(response.status_code, 400)

    def test_post_receita(self):
        response = client.post(reverse("receita-list"), {'nome': 'Bolinho', 'descricao': 'pequeno bolo'})
        self.assertEqual(response.status_code, 201)
        receita = client.get(reverse("receita-list"), response.data)
        self.assertEqual(receita.data[0], response.data)
