BASE_URL = 'https://reqres.in/'

def check_code_response(response, status_code) -> None:
    assert status_code == response.status_code