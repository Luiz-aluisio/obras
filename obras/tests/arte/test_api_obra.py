from django.urls import reverse


def test_listar_obras_200(client_logged):
    resp = client_logged.get(reverse('obra-list'))
    assert resp.status_code == 200


def test_inserir_obra_sem_campos_obrigatorios(client_logged):
    resp = client_logged.post(reverse('obra-list'))
    resultado = resp.json()
    obrigatorio = ['Este campo é obrigatório.']
    esperado = {
        'nome': obrigatorio,
        'descricao': obrigatorio,
    }

    assert resultado == esperado


def test_inserir_obra_com_descricao_mais_240_caractereres(
    client_logged, faker
):
    entrada = {
        'nome': faker.name(),
        'data_de_exposicao': '2023-11-27',
        'descricao': faker.text(300),
    }

    resp = client_logged.post(reverse('obra-list'), data=entrada)
    resultado = resp.json()
    esperado = {
        'descricao': [
            'Certifique-se de que este campo não tenha mais de 240 caracteres.'
        ],
    }
    assert resultado == esperado


def test_inserir_obra_sem_data_exposicao_ou_publicacao(client_logged, faker):
    entrada = {
        'nome': faker.name(),
        'descricao': faker.text(100),
    }
    resp = client_logged.post(reverse('obra-list'), data=entrada)
    resultado = resp.json()
    esperado = {
        'data_de_exposicao': [
            'obrigatoria caso a data de publicacao nao seja informada'
        ],
        'data_de_publicacao': [
            'obrigatoria caso a data de exposicao não seja informada'
        ],
    }

    assert resultado == esperado
