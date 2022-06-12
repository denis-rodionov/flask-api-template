import json

from tests.test_config import client, todo_service


def test_get_all(client, todo_service):
    # given
    todo_service.get_all.return_value = [
        {'title': '1'}, {'title':'2'}
    ]
    # when
    response = client.get('/todo')
    # then
    assert response.status_code == 200
    assert len(response.json['todo_list']) == 2
    todo_service.get_all.assert_any_call()


def test_post(client, todo_service):
    # given
    todo_service.add.return_value = None
    data = {'title': 'test-title'}
    # when
    response = client.post('/todo', json=data)
    # then
    assert response.status_code == 201
    todo_service.add.assert_any_call(data)
