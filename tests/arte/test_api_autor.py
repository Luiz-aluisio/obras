def test_listar_autores_200(client, django_user_model):
    username = 'admin'
    password = 'admin'
    user = django_user_model.objects.create_user(
        username=username, password=password
    )
    client.force_login(user)
    resp = client.get('/api/autor/')
    assert resp.status_code == 200
