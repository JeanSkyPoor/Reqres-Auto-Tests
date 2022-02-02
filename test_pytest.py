import requests
from secondary_func import *
from env_variables import *
import allure
import pytest


@allure.step('start connection')
@pytest.mark.regression
@allure.severity(allure.severity_level.MINOR)
def test_get_list_users():
    response = requests.get(f'{BASE_URL}api/users?page=2')

    check_code_response(response, 200)
    response = response.json()

    assert len(response['data']) == 6


@pytest.mark.regression
@allure.severity(allure.severity_level.CRITICAL)
def test_get_single_user():
    response = requests.get(f'{BASE_URL}api/users/2')

    check_code_response(response, 200)
    response = response.json()

    assert response['data']['id'] == 2
    assert response['data']['first_name'] == 'Janet'
    assert response['data']['last_name'] == 'Weaver'


@pytest.mark.regression
@allure.severity(allure.severity_level.MINOR)
def test_get_single_user_not_found():
    response = requests.get(f'{BASE_URL}api/users/23')

    check_code_response(response, 404)


@pytest.mark.regression
@allure.severity(allure.severity_level.MINOR)
def test_post_create():
    response = requests.post(f'{BASE_URL}api/users', data=read_and_return_data('post_create', DATA_REQUEST_FILE_NAME))

    check_code_response(response, 201)
    response = response.json()

    assert response['name'] == 'morpheus'
    assert response['job'] == 'leader'
    assert len(response) == 4


@pytest.mark.regression
@allure.severity(allure.severity_level.MINOR)
def test_put_update():
    response = requests.put(f'{BASE_URL}api/users/2', data=read_and_return_data('put_update', DATA_REQUEST_FILE_NAME))

    check_code_response(response, 200)
    response = response.json()

    assert response['job'] == 'zion resident'


@pytest.mark.regression
@allure.severity(allure.severity_level.MINOR)
def test_delete_user():
    response = requests.delete(f'{BASE_URL}api/users/2')

    check_code_response(response, 204)


@pytest.mark.regression
@allure.severity(allure.severity_level.MINOR)
def test_post_register_successful():
    response = requests.post(f'{BASE_URL}api/register',
                             data=read_and_return_data('post_register_successful', DATA_REQUEST_FILE_NAME))

    check_code_response(response, 200)
    response = response.json()

    assert response['id'] is not None


@pytest.mark.regression
@allure.severity(allure.severity_level.MINOR)
def test_post_register_unsuccessful():
    response = requests.post(f'{BASE_URL}api/register',
                             data=read_and_return_data('post_register_unsuccessful', DATA_REQUEST_FILE_NAME))

    check_code_response(response, 400)
    response = response.json()

    assert response['error'] == 'Missing password'


@pytest.mark.regression
@allure.severity(allure.severity_level.MINOR)
def test_post_login_successful():
    response = requests.post(f'{BASE_URL}api/login',
                             data=read_and_return_data('post_login_successful', DATA_REQUEST_FILE_NAME))

    check_code_response(response, 200)
    response = response.json()

    assert response['token'] is not None


@pytest.mark.regression
@allure.severity(allure.severity_level.MINOR)
def test_post_login_unsuccessful():
    response = requests.post(f'{BASE_URL}api/login',
                             data=read_and_return_data('post_login_unsuccessful', DATA_REQUEST_FILE_NAME))
    check_code_response(response, 400)
    response = response.json()

    assert response['error'] == 'Missing password'
