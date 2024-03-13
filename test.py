import pytest
from unittest.mock import MagicMock
from app import fetch_pokemon_data, get_pokemon_names

@pytest.fixture
def requests_mock(mocker):
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "results": [
            {"name": "bulbasaur"},
            {"name": "charmander"},
            {"name": "squirtle"}
        ]
    }
    return mocker.patch('main.requests.get', return_value=mock_response)

def test_fetch_pokemon_data_success(requests_mock):
    data = fetch_pokemon_data()
    assert data == {
        "results": [
            {"name": "bulbasaur"},
            {"name": "charmander"},
            {"name": "squirtle"}
        ]
    }

def test_get_pokemon_names(requests_mock):
    data = fetch_pokemon_data()
    names = get_pokemon_names(data)
    expected_names = ["bulbasaur", "charmander", "squirtle"]
    assert names == expected_names
