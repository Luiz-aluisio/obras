import pytest
from django.core.exceptions import ValidationError

def test_adicionar_autor(db, autor):
    autor.save()

    assert autor.id == 1

def teste_autor_nao_brasileiro_com_cpf(db,autor):
    autor.cpf ='817.827.830-83'
    with pytest.raises(ValidationError):
        autor.save()

def teste_autor_brasileiro_sem_cpf(db,autor):
    autor.nacionalidade = 'BR'
    with pytest.raises(ValidationError):
        autor.save()
        