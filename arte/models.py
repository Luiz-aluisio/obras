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
    cpf = CPFField(masked=True, unique=True, null=True, blank=True)

    def __str__(self):
        return self.nome

    def clean(self):
        if self.nacionalidade.code == 'BR' and not self.cpf:
            raise ValidationError({'cpf': _('se nacionalidade brasil cpf obrigatorio')})
        if self.nacionalidade.code != 'BR' and self.cpf:
            raise ValidationError({'cpf': _('cpf somente para nacionalidade brasil')})
        return super().clean()
    
    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        if self.obras.exists():
            raise ValidationError(_('autor não pode ser excluido pois possui obras'))
        return super().delete(*args, **kwargs)


class Obra(models.Model):
    nome = models.CharField(max_length=128,null=False,blank=False)
    descricao = models.CharField(max_length=240,null=False,blank=False)
    data_de_publicacao = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    data_de_exposicao = models.DateField(auto_now=False, auto_now_add=False,null=True,blank=True)
    autores = models.ManyToManyField(Autor, related_name='obras', null=True, blank=True)
    
    def __str__(self):
        return self.nome

    def clean(self):
        if self.data_de_exposicao is None and self.data_de_publicacao is None:
            raise ValidationError(
                {
                    'data_de_exposicao': _('obrigatoria caso a data de publicacao nao seja informada'),
                    'data_de_publicao':_('obrigatoria caso a data de exposicao não seja informada'),
                }
            )
        return super().clean()
    
    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)
    
