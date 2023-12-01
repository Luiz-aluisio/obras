import pytest
from django.core.exceptions import ValidationError
from model_bakery import baker


def test_adicionar_autor(db):
    autor = baker.make('arte.Autor')

    assert autor.id == 1


def teste_autor_nao_brasileiro_com_cpf(db):
    with pytest.raises(ValidationError) as excinfo:
        baker.make('arte.Autor', cpf='817.827.830-83', nacionalidade='MX')

    assert 'cpf somente para nacionalidade brasil' in str(excinfo.value)


def teste_autor_brasileiro_sem_cpf(db):
    with pytest.raises(ValidationError) as excinfo:
        baker.make('arte.Autor', nacionalidade='BR')

    assert 'se nacionalidade brasil cpf obrigatorio' in str(excinfo.value)


def test_remover_autor_com_obra(db, autor_com_obra):
    with pytest.raises(ValidationError) as excinfo:
        autor_com_obra.delete()

    assert 'autor não pode ser excluido pois possui obras' in str(
        excinfo.value
    )


def test_adcionar_obra_sem_data_de_publicacao_ou_data_de_exposicao():
    with pytest.raises(ValidationError) as excinfo:
        baker.make('arte.Obra')

    assert 'obrigatoria caso a data de publicacao nao seja informada' in str(
        excinfo.value
    )
    assert 'obrigatoria caso a data de exposicao não seja informada' in str(
        excinfo.value
    )
