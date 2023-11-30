from datetime import date, timedelta

from django.urls import reverse
from model_bakery import baker
from pytest import dict_remove_none

from obras.arte.serializers import AutorSerializer


def test_campos_obrigatorio(client_logged):
    resp = client_logged.post(reverse('autor-list'), data={})
    campos = resp.json()
    esperado = ['Este campo é obrigatório.']
    assert campos['data_nascimeto'] == esperado
    assert campos['nacionalidade'] == esperado
    assert campos['sexo'] == esperado
    assert campos['nome'] == esperado


def test_listar_autores_200(client_logged):
    resp = client_logged.get(reverse('autor-list'))
    assert resp.status_code == 200


def test_email_invalido(client_logged):
    resp = client_logged.post(
        reverse('autor-list'), data={'email': 'email invalido'}
    )
    campos = resp.json()
    esperado = ['Insira um endereço de email válido.']
    assert campos['email'] == esperado


def test_cpf_obrigatorio_nacionalidade_brasil(client_logged):
    entrada = {
        'nome': 'Monteiro Lobato',
        'sexo': 'M',
        'data_nascimeto': '1882-04-18',
        'nacionalidade': 'BR',
    }
    resp = client_logged.post(reverse('autor-list'), data=entrada)
    campos = resp.json()
    esperado = ['se nacionalidade brasil cpf obrigatorio']
    assert campos['cpf'] == esperado


def test_nao_brasileiro_com_cpf(client_logged):
    entrada = {
        'nome': 'Mariah Isabelle Mariah Rezende',
        'cpf': '585.479.126-90',
        'data_nascimeto': '1963-09-06',
        'sexo': 'F',
        'nacionalidade': 'MX',
    }
    resp = client_logged.post(reverse('autor-list'), data=entrada)
    campos = resp.json()
    esperado = {'cpf': ['cpf somente para nacionalidade brasil']}
    assert campos == esperado


def test_email_duplicado(client_logged, autor):
    entrada = {
        'nome': 'Monteiro Lobato',
        'sexo': 'M',
        'data_nascimeto': '1882-04-18',
        'nacionalidade': 'BR',
        'cpf': '585.479.126-90',
        'email': 'gabriel@email.com',
    }
    autor.save()
    resp = client_logged.post(reverse('autor-list'), data=entrada)
    resultado = resp.json()
    esperado = {'email': ['autor com este email já existe.']}
    assert resultado == esperado


def test_cpf_duplicado(client_logged, autor):
    autor.nacionalidade = 'BR'
    autor.cpf = '585.479.126-90'
    autor.save()
    entrada = {
        'nome': 'Monteiro Lobato',
        'sexo': 'M',
        'data_nascimeto': '1882-04-18',
        'nacionalidade': 'BR',
        'cpf': '585.479.126-90',
    }

    resp = client_logged.post(reverse('autor-list'), data=entrada)
    resultado = resp.json()
    esperado = {'cpf': ['autor com este cpf já existe.']}
    assert resultado == esperado


def test_nacionalidade_invalido(client_logged):
    resp = client_logged.post(
        reverse('autor-list'), data={'nacionalidade': 'ZZ'}
    )
    resultado = resp.json()
    esperado = {'nacionalidade': ['"ZZ" não é um escolha válido.']}
    assert resultado.items() >= esperado.items()


def test_data_nacimento_futura(client_logged):
    hoje = date.today()
    um_dia = timedelta(days=1)
    amanha = hoje + um_dia
    autor = baker.make('arte.Autor', data_nascimeto=amanha)
    entrada = dict_remove_none(AutorSerializer(autor).data)

    resp = client_logged.post(reverse('autor-list'), data=entrada)
    resultado = resp.json()
    esperado = {
        'data_nascimeto': [
            f'Certifique-se que este valor seja menor ou igual a {hoje}.'
        ]
    }
    assert resultado == esperado


def test_remover_autor_com_obra(client_logged):
    obras = baker.prepare(
        'arte.Obra', data_de_exposicao='2020-12-31', _quantity=1
    )
    autor = baker.make('arte.Autor', obras=obras)

    url = reverse('autor-list') + str(autor.id) + '/'
    resp = client_logged.delete(url)
    resultado = resp.json()
    esperado = {'autor': ['autor não pode ser excluido pois possui obras']}
    assert resultado == esperado