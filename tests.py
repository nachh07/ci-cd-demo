import pytest
from unittest.mock import MagicMock
from app import fetch_pokemon_data, get_pokemon_names

@pytest.fixture
def requests_mock():
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "results": [
            {"name": "bulbasaur"},
            {"name": "charmander"},
            {"name": "squirtle"}
        ]
    }
    return mock_response

def test_fetch_pokemon_data_success(requests_mock):
    data = fetch_pokemon_data("http://pokeapi.co/api/v2/pokemon/")
    assert data == {
        "results": [
            {"name": "bulbasaur"},
            {"name": "charmander"},
            {"name": "squirtle"}
        ]
    }

def test_get_pokemon_names(requests_mock):
    data = fetch_pokemon_data("http://pokeapi.co/api/v2/pokemon/")
    names = get_pokemon_names(data)
    expected_names = ["bulbasaur", "charmander", "squirtle"]
    assert names == expected_names
