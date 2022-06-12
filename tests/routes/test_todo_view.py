from tests.test_config import client


def test_get_all(client):
    response = client.get('/todo')

    assert response.status_code == 200
    assert len(response.json['todo_list']) == 2
