from django.contrib.auth.models import AbstractUser
from django.db import models

PERMISSOES = (
    ('PROFESSOR', 'Professor'),
    ('ALUNO', 'Aluno'),
)

class Usuario(AbstractUser):
    role = models.CharField(max_length=20, choices=PERMISSOES, default='ALUNO')
