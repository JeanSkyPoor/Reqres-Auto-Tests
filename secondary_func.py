import json


def check_code_response(response, status_code: int) -> None:
    """
    match response.status_code and entered code

    response: response not in json format
    status code: int object
    """
    assert response.status_code == status_code 


def read_and_return_data(name_func: str, name_file: str) -> dict:
    """
    Return correct data for func from name_file
    
    name_func: key for dict (for example "get_sigle_user_not_found")
    name_file: name of your file with data (for example "data.json")
    """
    with open(f"{name_file}", 'r') as f:
        data = json.load(f)
        return data[name_func][0]