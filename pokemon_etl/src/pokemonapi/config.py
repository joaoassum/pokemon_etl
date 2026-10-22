import os
from pathlib import Path

from dotenv import load_dotenv

# Diretório raiz do projeto
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Variáveis de ambiente
load_dotenv(BASE_DIR / "config" / ".env")

URL_POKE_API = os.getenv(
    "URL_POKE_API",
    "https://pokeapi.co/api/v2/pokemon"
)

# Diretórios das camadas
DATA_DIR = BASE_DIR / "data"

BRONZE_DIR = DATA_DIR / "bronze"
SILVER_DIR = DATA_DIR / "silver"
GOLD_DIR = DATA_DIR / "gold"

# Diretórios dos Pokémon
POKEMONS_BRONZE_LIST_PATH = BRONZE_DIR / "pokemons"
POKEMONS_SILVER_LIST_PATH = SILVER_DIR / "pokemons"
POKEMONS_GOLD_LIST_PATH = GOLD_DIR / "pokemons"
BRONZE_POKEMONS_FILE = BRONZE_DIR / "pokemon.json"

# Resumo e dados tratados
SILVER_CLEAN_DATA_DIR = SILVER_DIR / "clean_data"
GOLD_CLEAN_DATA_DIR = GOLD_DIR / "clean_data"
SILVER_POKEMONS_SUMMARY_FILE = (
    SILVER_CLEAN_DATA_DIR / "summary_pokemons.parquet"
)
