from django.db import models


class Tratamentos(models.Model):
    paciente = models.CharField(max_length=150)
    am = models.CharField(max_length=150)
    duracao = models.IntegerField()