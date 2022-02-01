def check_code_response(response, status_code) -> None:
    assert status_code == response.status_code