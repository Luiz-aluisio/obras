def test_campos_obrigatorio(client_logged):
    resp = client_logged.post('/api/autor/', data={})
    campos = resp.json()
    esperado = ['Este campo é obrigatório.']
    assert campos['data_nascimeto'] == esperado
    assert campos['nacionalidade'] == esperado
    assert campos['sexo'] == esperado
    assert campos['nome'] == esperado


def test_listar_autores_200(client_logged):
    resp = client_logged.get('/api/autor/')
    assert resp.status_code == 200


def tes_email_invalido(client_logged):
    resp = client_logged.post('/api/autor/', data={'email': 'email invalido'})
    campos = resp.json()
    esperado = ['Insira um endereço de email válido.']
    assert campos['email'] == esperado

def tes_cpf_obrigatorio_nacionalidade_brasil(client_logged):
    entrada = {'nome': 'Monteiro Lobato',
               'sexo':'M',
               'data_nascimento':'1882-04-18',
               'nacionalidade': 'BR'}
    resp = client_logged.post('/api/autor/',data=entrada)
    campos = resp.json()
    esperado = []
    assert campos['cpf'] == esperado