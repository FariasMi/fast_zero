from http import HTTPStatus


def test_read_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get('/')  # fase de ação, execução. ACT

    assert response.status_code == HTTPStatus.OK  # afirmação ASSERT
    assert response.json() == {'message': 'Olá Mundo!'}


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'Alana',
            'email': 'alana@example.com',
            'password': 'alana123',
        },
    )

    # Retornou o status code correto?
    assert response.status_code == HTTPStatus.CREATED

    # Validar o UserPublic
    assert response.json() == {
        'id': 1,
        'username': 'Alana',
        'email': 'alana@example.com',
    }


def test_get_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [{'id': 1, 'username': 'Alana', 'email': 'alana@example.com'}]
    }


def test_get_user_by_id(client):
    response = client.get('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'username': 'Alana',
        'email': 'alana@example.com',
    }


def test_get_user_by_id_not_found(client):
    response = client.get('/users/2')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_put_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'Alanita',
            'email': 'alanita@example.com',
            'password': 'alana123@',
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'username': 'Alanita',
        'email': 'alanita@example.com',
    }


def test_put_user_not_found(client):
    response = client.put(
        '/users/2',
        json={
            'username': 'Alanita',
            'email': 'alanita@example.com',
            'password': 'alana123@',
        },
    )

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_user_delete(client):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted!'}


def test_user_delete_not_found(client):
    response = client.delete('/users/2')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}
