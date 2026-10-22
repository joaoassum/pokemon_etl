import pandas as pd

from pokemonapi.config import SILVER_POKEMONS_SUMMARY_FILE

# =========================
# SILVER: limpeza e estruturação
# =========================

def limpar_colunas_bronze(pokemons: list[dict]) -> pd.DataFrame:
    """Remove campos desnecessários dos dados brutos."""

    df = pd.DataFrame(pokemons)

    colunas_remover = [
        "past_types",
        "sprites",
        "cries",
        "abilities",
        "past_abilities",
        "game_indices",
        "held_items",
        "forms",
        "moves",
        "past_stats",
        "is_default",
        "species",
        "location_area_encounters",
    ]

    return df.drop(columns=colunas_remover, errors="ignore")


def tratar_campos_summary(pokemons: pd.DataFrame) -> pd.DataFrame:
    """Transforma stats e types aninhados em colunas simples."""

    df = pokemons.copy()

    # Transformar os atributos (stats) em colunas
    for index, stats in df["stats"].items():
        for informacao in stats:
            nome = informacao["stat"]["name"].replace("-", "_")
            valor = informacao["base_stat"]

            df.loc[index, nome] = valor

    # Transformar os tipos em tipo_1 e tipo_2
    df["tipo_1"] = None
    df["tipo_2"] = None

    for index, types in df["types"].items():
        for tipo in types:
            nome = f"tipo_{tipo['slot']}"
            valor = tipo["type"]["name"]

            df.loc[index, nome] = valor

    # Remover as estruturas aninhadas já tratadas
    return df.drop(columns=["stats", "types"])


# =========================
# GOLD: análises e rankings
# =========================

def summary_type_stats(pokemons: pd.DataFrame) -> pd.DataFrame:
    """Conta quantos Pokémon pertencem a cada tipo."""

    tipos = pd.concat(
        [pokemons["tipo_1"], pokemons["tipo_2"]],
        ignore_index=True,
    ).dropna()

    return (
        tipos.value_counts()
        .rename_axis("tipo")
        .reset_index(name="quantidade")
    )


def criar_ranking_por_status_summary(
    status: str,
    tamanho_ranking: int,
) -> pd.DataFrame:
    """Retorna os Pokémon com os maiores valores de determinado atributo."""

    if tamanho_ranking <= 0:
        raise ValueError("O tamanho do ranking deve ser maior que zero.")

    # Lista permitida para evitar nomes de colunas inválidos
    status_permitidos = {
        "attack",
        "hp",
        "defense",
        "special_attack",
        "special_defense",
        "speed",
        "weight",
        "height",
    }

    if status not in status_permitidos:
        raise ValueError(f"Status inválido: {status}")

    df = pd.read_parquet(SILVER_POKEMONS_SUMMARY_FILE)

    colunas = ["id", "name", status, "tipo_1", "tipo_2"]

    return (
        df.sort_values(
            by=status,
            ascending=False,
        )
        .head(tamanho_ranking)
        .loc[:, colunas]
        .reset_index(drop=True)
    )
