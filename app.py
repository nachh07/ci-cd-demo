import logging
import requests 

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def fetch_pokemon_data(url: str) -> dict | None:
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Error al obtener datos de la API: {e}")
        return None

def get_pokemon_names(data: dict) -> list:
    if data:
        return [pokemon['name'] for pokemon in data.get('results', [])]
    else:
        return []

def main():
    data = fetch_pokemon_data(url)
    pokemons = get_pokemon_names(data)
    if pokemons:
        logger.info("Lista de Pokemones obtenida exitosamente:")
        for pokemon in pokemons:
            logger.info(pokemon)
    else:
        logger.warning("No se pudieron obtener los datos de la API.")

if __name__ == "__main__":
    url = "http://pokeapi.co/api/v2/pokemon/"
    main()