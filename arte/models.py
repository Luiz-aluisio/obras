from collections.abc import Iterable
from django.db import models
from django_countries.fields import CountryField
from django_cpf_cnpj.fields import CPFField


class Autor(models.Model):
    nome = models.CharField(max_length=128, null=False, blank=False)
    sexo = models.CharField(max_length=1, choices=[('F', 'Femino'), ('M', 'Masculino')])
    email = models.EmailField(unique=True, null=True, blank=True, max_length=254)
    data_nascimeto = models.DateField(auto_now=False, auto_now_add=False)
    nacionalidade = CountryField()
    cpf = CPFField(masked=True, unique=True)

    def save(self, *args, **kwargs):
        if self.nacionalidade.code == 'BR' and not self.cpf:
            raise ValueError('se nacionalidade brasil cpf nescesario')
        if self.nacionalidade.code != 'BR' and self.cpf:
            raise ValueError('cpf nescesario se nacionalidade for brasil')
        return super().save(*args, **kwargs)

