from pokemonapi.config import (
    POKEMONS_GOLD_LIST_PATH,
    POKEMONS_SILVER_LIST_PATH,
    SILVER_CLEAN_DATA_DIR,
)
from pokemonapi.extract import extract_pokemons_details
from pokemonapi.load import (
    salvar_pokemons_silver,
    salvar_ranking_gold,
    salvar_summary_silver,
    salvar_summary_types_gold,
)
from pokemonapi.transform import (
    criar_ranking_por_status_summary,
    limpar_colunas_bronze,
    summary_type_stats,
    tratar_campos_summary,
)


def main() -> None:
    # 1. EXTRAÇÃO: API -> Bronze
    extract_pokemons_details()

    # 2. LEITURA DA BRONZE
    from pokemonapi.extract import load_pokemons_from_bronze

    pokemons = load_pokemons_from_bronze()

    # 3. SILVER: limpeza e estruturação
    pokemons_limpos = limpar_colunas_bronze(pokemons)

    pokemons_summary = tratar_campos_summary(pokemons_limpos)

    # 4. LOAD: gravação da Silver
    salvar_pokemons_silver(
        pokemons_limpos,
        POKEMONS_SILVER_LIST_PATH,
    )

    salvar_summary_silver(
        pokemons_summary,
        SILVER_CLEAN_DATA_DIR,
    )

    # 5. GOLD: geração de análises
    resumo_tipos = summary_type_stats(pokemons_summary)

    salvar_summary_types_gold(
        resumo_tipos,
        POKEMONS_GOLD_LIST_PATH,
    )

    # 6. GOLD: rankings por atributo
    stats = [
        "attack",
        "hp",
        "defense",
        "special_attack",
        "special_defense",
        "speed",
        "weight",
        "height",
    ]

    tamanho_ranking = 10

    for status in stats:
        ranking = criar_ranking_por_status_summary(
            status,
            tamanho_ranking,
        )

        salvar_ranking_gold(
            ranking,
            status,
            POKEMONS_GOLD_LIST_PATH,
        )


if __name__ == "__main__":
    main()
