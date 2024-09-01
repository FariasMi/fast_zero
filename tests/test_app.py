from http import HTTPStatus


def test_read_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get('/')  # fase de ação, execução. ACT

    assert response.status_code == HTTPStatus.OK  # afirmação ASSERT
    assert response.json() == {'message': 'Olá Mundo!'}
