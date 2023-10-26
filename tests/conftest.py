import pytest
from arte.models import Autor


@pytest.fixture
def autor():
    return Autor(
        nome='Fernando Pessoa',
        sexo='M',
        email= 'gabriel@email.com',
        data_nascimeto='1927-03-06',
        nacionalidade='ME',
    )