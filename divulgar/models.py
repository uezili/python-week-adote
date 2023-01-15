from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Raca(models.Model):

    raca = models.CharField(max_length=255)

    def __str__(self):
        return self.raca


class Tag(models.Model):

    tag = models.CharField(max_length=240)

    def __str__(self):
        return self.tag


class Pet(models.Model):

    choices_status = (('P', 'Para adoção'),
                      ('A', 'Adotado'))
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    foto = models.ImageField(upload_to="foto_pets")
    nome = models.CharField(max_length=100)
    descrição = models.TextField()
    estado = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    telefone = models.CharField(max_length=14)
    tag = models.ManyToManyField(Tag)
    raca = models.ForeignKey(Raca, on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=1, choices=choices_status)

    def __str__(self):
        return self.nome
