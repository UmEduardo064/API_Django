from django.db import models

class Grupo(models.Model):
    nome = models.CharField(max_length=50, blank=False, null=False)
    descricao = models.CharField(max_length=500, blank=False, null=False)
    proprietario = models.ForeignKey('accounts.usuario', on_delete=models.CASCADE, related_name='grupos')

    def __str__(self):
        return self.nome

class Material(models.Model):
    titulo = models.CharField(max_length=100, blank=False, null=False)
    conteudo = models.CharField(max_length=5000, blank=False, null=False)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, related_name='materiais')

    def __str__(self):
        return self.titulo
