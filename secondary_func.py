import json

def check_code_response(response, status_code) -> None:
    assert status_code == response.status_code

def read_and_return_data(name_func):
    """
    Return correct data for func from data.json file
    """
    with open("data.json", 'r') as f:
        data = json.load(f)
        return data[name_func][0]