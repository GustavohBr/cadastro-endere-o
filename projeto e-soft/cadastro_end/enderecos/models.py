from django.db import models

class Enderecos(models.Model):
    cep = models.CharField(max_length=9)
    endereço = models.CharField(max_length=100)
    numero = models.CharField(max_length=100)
    complemento = models.CharField(max_length=100, null=True, blank=True)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    UF = models.CharField(max_length=100)
    descriçao = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.cep