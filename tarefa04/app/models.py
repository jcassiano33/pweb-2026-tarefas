from django.db import models

class Tarefa(models.Model):
    nome = models.CharField(max_length=100)
    status = models.BooleanField()
    prazo = models.CharField(max_length=100)