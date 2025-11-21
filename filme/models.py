from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser



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
    data_criacao = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.titulo  # nome legível no painel admin


class Episodio(models.Model):
    filme = models.ForeignKey("Filme", related_name="episodios", on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    video = models.URLField()


    def save(self, *args, **kwargs):
        # Converte automaticamente o link normal do YouTube em embed
        if "watch?v=" in self.video:
            self.video = self.video.replace("watch?v=", "embed/")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.filme.titulo} - {self.titulo}"




class Usuario(AbstractUser):
    filmes_vistos = models.ManyToManyField("Filme")

#depois de criar modelo. registre no admin

class Perfil(models.Model):
    user = models.OneToOneField(
        Usuario,
        on_delete=models.CASCADE,
        related_name="perfil"
    )
    foto = models.ImageField(upload_to="fotos/", blank=True, null=True)

    def __str__(self):
        return f"Perfil de {self.user.username}"

from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=Usuario)
def criar_perfil(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(user=instance)
