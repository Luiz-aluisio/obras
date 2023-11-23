import pytest

from arte.models import Autor, Obra


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
