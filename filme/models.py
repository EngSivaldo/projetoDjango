from django.db import models
from django.utils import timezone


# Create your models here.

LISTA_CATEGORIAS = (
    ("ANALISES", "Análise"),
    ("PROGRAMACAO", "Programação"),
    ("APRESENTACAO", "Apresentação"),
    ("OUTROS", "Outros"),




)

# Modelo Filme
class Filme(models.Model):
    titulo = models.CharField(max_length=100)  # título do filme
    thumb = models.ImageField(upload_to='thumb_filmes')  # imagem de capa (miniatura)
    descricao = models.TextField()  # descrição do filme
    categoria = models.CharField(
        max_length=50,
        choices=LISTA_CATEGORIAS,
        default='OUTROS'
    )  # categoria com base na lista acima
    visualizacoes = models.IntegerField(default=0)  # número de visualizações
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo  # nome legível no painel admin
