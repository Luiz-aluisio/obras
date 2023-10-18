from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from django_cpf_cnpj.fields import CPFField


class Autor(models.Model):
    nome = models.CharField(max_length=128, null=False, blank=False)
    sexo = models.CharField(max_length=1, choices=[('F', 'Femino'), ('M', 'Masculino')])
    email = models.EmailField(unique=True, null=True, blank=True, max_length=254)
    data_nascimeto = models.DateField(auto_now=False, auto_now_add=False)
    nacionalidade = CountryField()
    cpf = CPFField(masked=True, unique=True)

    def clean(self):
        if self.nacionalidade.code == 'BR' and not self.cpf:
            raise ValidationError({'cpf': _('se nacionalidade brasil cpf obrigatorio')})
        if self.nacionalidade.code != 'BR' and self.cpf:
            raise ValidationError({'cpf': _('cpf somente para nacionalidade brasil')})
