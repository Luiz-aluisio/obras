import pytest

from arte.models import Autor, Obra


def pytest_configure():
    pytest.dict_remove_none = dict_remove_none


@pytest.fixture
def autor():
    return Autor(
        nome='Fernando Pessoa',
        sexo='M',
        email='gabriel@email.com',
        data_nascimeto='1927-03-06',
        nacionalidade='ME',
    )


@pytest.fixture
def obra(db):
    obra = Obra(
        nome='O mundo de sofia',
        descricao='conta historia da filosofia',
        data_de_publicacao='1991-12-05',
    )
    obra.save()

    return obra


@pytest.fixture
def client_logged(client, django_user_model):
    username = 'admin'
    password = 'admin'
    user = django_user_model.objects.create_user(
        username=username, password=password
    )
    client.force_login(user)
    return client


def dict_remove_none(data):
    return {key: value for key, value in data.items() if value is not None}
