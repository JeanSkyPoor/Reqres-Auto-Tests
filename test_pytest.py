import requests
from secondary_func import *


def test_get_list_users():
    response = requests.get(f'{BASE_URL}api/users?page=2')

    check_code_response(response, 200)
    response = response.json()

    assert len(response['data']) == 6


def test_get_single_user():
    response = requests.get(f'{BASE_URL}api/users/2')

    check_code_response(response, 200)
    response = response.json()

    assert response['data']['id'] == 2
    assert response['data']['first_name'] == 'Janet'
    assert response['data']['last_name'] == 'Weaver'


def test_get_sigle_user_not_found():
    response = requests.get(f'{BASE_URL}api/users/23')

    check_code_response(response, 404)


def test_post_create():
    response = requests.post(f'{BASE_URL}api/users', data={'name': 'morpheus', 
                                                                    'job': 'leader'})

    check_code_response(response, 201)
    response = response.json()

    assert response['name'] == 'morpheus'
    assert response['job'] == 'leader'
    assert len(response) == 4


def test_put_update():
    response = requests.put(f'{BASE_URL}api/users/2', data={'name': 'morpheus', 
                                                                    'job': 'zion resident'})

    check_code_response(response, 200)
    response = response.json()

    assert response['job'] == 'zion resident'


def test_delete_user():
    response = requests.delete(f'{BASE_URL}api/users/2')

    check_code_response(response, 204)


def test_post_register_successful():
    response = requests.post(f'{BASE_URL}api/register', data={'email': 'eve.holt@reqres.in',
                                                                        'password': 'pistol'})

    check_code_response(response, 200)
    response = response.json()

    assert response['id'] is not None


def test_post_register_unsuccessful():
    response = requests.post(f'{BASE_URL}api/register', data={'email': 'sydney@fife'})

    check_code_response(response, 400)
    response = response.json()

    assert response['error'] == 'Missing password'


def test_post_login_successful():
    response = requests.post(f'{BASE_URL}api/login', data={'email': 'eve.holt@reqres.in',
                                                                        'password': 'cityslicka'})
                                                                        
    check_code_response(response, 200)
    response = response.json()

    assert response['token'] is not None


def test_post_login_unsuccessful():
    response = requests.post(f'{BASE_URL}api/login', data={'email': 'peter@klaven'})
    check_code_response(response, 400)
    response = response.json()

    assert response['error'] == 'Missing password'