import pytest
from model_bakery import baker


def dict_remove_none(data):
    return {key: value for key, value in data.items() if value is not None}


def pytest_configure():
    pytest.dict_remove_none = dict_remove_none


@pytest.fixture
def autor_com_obra(db):
    obras = baker.prepare(
        'arte.Obra', data_de_exposicao='2020-12-31', _quantity=1
    )
    return baker.make('arte.Autor', obras=obras)


@pytest.fixture
def client_logged(client, django_user_model):
    username = 'admin'
    password = 'admin'
    user = django_user_model.objects.create_user(
        username=username, password=password
    )
    client.force_login(user)
    return client
