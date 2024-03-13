# test_main.py
import pytest
from app import fetch_pokemon_data, get_pokemon_names

@pytest.fixture
def mock_fetch_pokemon_data(requests_mock):
    mock_response = {
        "results": [
            {"name": "bulbasaur"},
            {"name": "charmander"},
            {"name": "squirtle"}
        ]
    }
    requests_mock.get("http://pokeapi.co/api/v2/pokemon/", json=mock_response)
    return mock_response

def test_fetch_pokemon_data_success(mock_fetch_pokemon_data):
    data = fetch_pokemon_data()
    assert data == mock_fetch_pokemon_data

def test_get_pokemon_names(mock_fetch_pokemon_data):
    names = get_pokemon_names(mock_fetch_pokemon_data)
    expected_names = ["bulbasaur", "charmander", "squirtle"]
    assert names == expected_names
