from django.db import models

# Create your models here.


class Receita(models.Model):

    class Meta:
        db_table = 'receita'

    nome = models.CharField(max_length=64)
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nome}: {self.descricao}"