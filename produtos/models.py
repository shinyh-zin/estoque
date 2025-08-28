from django.db import models

# Create your models here.
class Produtos(models.Model):
    nome = models.CharField(max_length=100)
    preço = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.IntegerField()
    descricao = models.TextField(blank=True)
    