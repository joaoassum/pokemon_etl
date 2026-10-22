import json

import requests

from pokemonapi.config import (
    BRONZE_POKEMONS_FILE,
    POKEMONS_BRONZE_LIST_PATH,
    URL_POKE_API,
)
from pokemonapi.load import salvar_json


def extract_pokemon_from_api() -> list[dict]:
    """Extrai a lista de Pokémon da PokéAPI, percorrendo a paginação."""

    pokemons = []
    url = URL_POKE_API

    with requests.Session() as session:
        while url:
            response = session.get(url, timeout=30)
            response.raise_for_status()

            dados = response.json()

            pokemons.extend(dados["results"])
            url = dados["next"]

    return pokemons


def extract_pokemons_details() -> None:
    """Salva o catálogo e os detalhes individuais na camada Bronze."""

    # Extrai e salva o catálogo
    pokemons = extract_pokemon_from_api()
    salvar_json(pokemons, BRONZE_POKEMONS_FILE)

    # Extrai os detalhes individuais
    with requests.Session() as session:
        for pokemon in pokemons:
            response = session.get(pokemon["url"], timeout=30)
            response.raise_for_status()

            pokemon_data = response.json()

            caminho = (
                POKEMONS_BRONZE_LIST_PATH
                / f"{pokemon_data['id']}.json"
            )

            salvar_json(pokemon_data, caminho)


def load_pokemons_from_bronze() -> list[dict]:
    """Lê os detalhes dos Pokémon armazenados na Bronze."""

    pokemons_list = []

    for arquivo in POKEMONS_BRONZE_LIST_PATH.glob("*.json"):
        with arquivo.open("r", encoding="utf-8") as file:
            pokemons_list.append(json.load(file))

    return pokemons_list