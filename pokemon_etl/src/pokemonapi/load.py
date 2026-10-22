import json
from pathlib import Path

import pandas as pd


def salvar_json(dados: dict | list, caminho: Path) -> None:
    caminho.parent.mkdir(parents=True, exist_ok=True)

    with caminho.open("w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=2)


def salvar_parquet(df: pd.DataFrame, caminho: Path) -> None:
    caminho.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(caminho, index=False)


def salvar_pokemons_silver(pokemons: pd.DataFrame, pasta: Path) -> None:
    pasta.mkdir(parents=True, exist_ok=True)

    for _, pokemon in pokemons.iterrows():
        caminho = pasta / f"{pokemon['id']}.parquet"
        salvar_parquet(pokemon.to_frame().T, caminho)


def salvar_summary_silver(df: pd.DataFrame, pasta: Path) -> None:
    salvar_parquet(df, pasta / "summary_pokemons.parquet")


def salvar_summary_types_gold(df: pd.DataFrame, pasta: Path) -> None:
    salvar_parquet(df, pasta / "summary_type.parquet")


def salvar_ranking_gold(
    df: pd.DataFrame,
    status: str,
    pasta: Path
) -> None:
    caminho = pasta / f"top_{len(df)}_{status}.parquet"
    salvar_parquet(df, caminho)