from http import HTTPStatus

from jwt import decode

from fast_zero.security import create_access_token, settings


def test_jwt_valid_token():
    data = {'sub': 'test@test.com'}
    token = create_access_token(data)

    result = decode(
        token,
        settings.SECRET_KEY,
        algorithms=[settings.ALGORITHM],
    )

    assert result['sub'] == data['sub']
    assert result['exp']


def test_token_invalido(client):
    response = client.delete(
        'users/1',
        headers={'Authorization': 'Bearer token erradasso'},
    )

    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {'detail': 'Could not validate credentials'}


def test_email_invalid(client):
    data = {}
    token = create_access_token(data)

    response = client.delete(
        'users/1',
        headers={'Authorization': f'{token}'},
    )

    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {'detail': 'Not authenticated'}
