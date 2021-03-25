from django.urls import path
from . import views

urlpatterns = [
    path('receitas/$', views.ReceitaList.as_view(), name='receita-list'),
]
