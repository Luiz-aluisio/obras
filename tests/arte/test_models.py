import pytest
from django.core.exceptions import ValidationError


def test_adicionar_autor(db, autor):
    autor.save()

    assert autor.id == 1


def teste_autor_nao_brasileiro_com_cpf(db, autor):
    autor.cpf = '817.827.830-83'
    with pytest.raises(ValidationError) as excinfo:
        autor.save()

    assert 'cpf somente para nacionalidade brasil' in str(excinfo.value)


def teste_autor_brasileiro_sem_cpf(db, autor):
    autor.nacionalidade = 'BR'
    with pytest.raises(ValidationError) as excinfo:
        autor.save()

    assert 'se nacionalidade brasil cpf obrigatorio' in str(excinfo.value)


def test_remover_autor_com_obra(db, autor, obra):
    autor.save()
    autor.obras.add(obra)

    with pytest.raises(ValidationError) as excinfo:
        autor.delete()

    assert 'autor não pode ser excluido pois possui obras' in str(
        excinfo.value
    )


def test_adcionar_obra_sem_data_de_publicacao_ou_data_de_exposicao(obra):
    obra.data_de_publicacao = None

    with pytest.raises(ValidationError) as excinfo:
        obra.save()

    assert 'obrigatoria caso a data de publicacao nao seja informada' in str(
        excinfo.value
    )
    assert 'obrigatoria caso a data de exposicao não seja informada' in str(
        excinfo.value
    )
