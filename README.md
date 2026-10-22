# Pokémon ETL Pipeline

Pipeline de Engenharia de Dados desenvolvido em Python utilizando a [PokeAPI](https://pokeapi.co/) como fonte de dados. O projeto tem como objetivo praticar a extração, transformação e organização de dados em diferentes camadas, seguindo os conceitos de arquitetura **Medallion (Bronze, Silver e Gold)**.

## Objetivos

- Consumir dados de uma API REST pública.
- Armazenar os dados brutos para processamento posterior.
- Limpar e estruturar os dados utilizando Pandas.
- Trabalhar com arquivos Parquet para armazenamento analítico.
- Criar conjuntos de dados agregados e rankings para análise.
- Organizar o código em módulos, separando extração, transformação e carregamento.

## Tecnologias utilizadas

- **Python** — linguagem principal.
- **Requests** — consumo da API REST.
- **Pandas** — manipulação e transformação dos dados.
- **PyArrow** — suporte à leitura e gravação de arquivos Parquet.
- **uv** — gerenciamento de dependências e ambiente Python.
- **python-dotenv** — gerenciamento de variáveis de ambiente.
- **Git e GitHub** — versionamento do código.

## Arquitetura do pipeline

O projeto utiliza três camadas de dados:

### Bronze — Dados brutos

Responsável por armazenar os dados extraídos da PokeAPI em formato JSON, preservando os dados originais para processamento posterior.

- Catálogo de Pokémon com nomes e URLs.
- Arquivos individuais com os detalhes de cada Pokémon.

### Silver — Dados tratados

Responsável pela limpeza, padronização e estruturação dos dados.

- Remoção de campos desnecessários para a análise.
- Extração dos atributos de combate, como ataque, defesa, velocidade e HP.
- Organização dos tipos de cada Pokémon.
- Armazenamento dos dados tratados em arquivos Parquet.

### Gold — Dados analíticos

Responsável por gerar conjuntos de dados preparados para consultas e análises.

- Resumo da quantidade de Pokémon por tipo.
- Ranking dos Pokémon com maiores valores de ataque.
- Rankings por HP, defesa, ataque especial, defesa especial, velocidade, peso e altura.

## Fluxo de processamento

```text
PokeAPI
   |
   v
Extract
   |
   v
Bronze - JSON
   |
   v
Transform
   |
   v
Silver - Parquet
   |
   v
Gold - Dados analíticos
   |
   v
Rankings e agregações
```

## Estrutura do projeto

```text
pokemon_etl/
├── config/
│   └── .env.example
├── data/
│   ├── bronze/
│   ├── silver/
│   └── gold/
├── src/
│   └── pokemonapi/
│       ├── __init__.py
│       ├── config.py
│       ├── extract.py
│       ├── transform.py
│       ├── load.py
│       └── main.py
├── .gitignore
├── pyproject.toml
├── uv.lock
└── README.md
```

> Os arquivos gerados nas camadas de dados são ignorados pelo Git para evitar o versionamento de grandes volumes de dados processados.

## Como executar

### 1. Pré-requisitos

- Python 3.13 ou superior.
- [uv](https://docs.astral.sh/uv/).
- Git.

### 2. Clone o repositório

```bash
git clone <URL_DO_REPOSITORIO>
cd pokemon_etl
```

### 3. Configure as variáveis de ambiente

Crie o arquivo `config/.env` com a URL da API:

```env
URL_POKE_API=https://pokeapi.co/api/v2/pokemon
```

O arquivo `.env` não deve ser enviado ao GitHub. Utilize `.env.example` para documentar as variáveis necessárias.

### 4. Instale as dependências

```bash
uv sync
```

### 5. Execute o pipeline

```bash
uv run python -m pokemonapi.main
```

Execute o comando a partir da raiz do projeto. Caso o pacote não esteja instalado ou configurado para execução dessa forma, verifique a configuração de build e o caminho de importação definido no `pyproject.toml`.

## Resultados esperados

Ao executar o pipeline, são gerados arquivos de dados nas seguintes camadas:

| Camada | Formato | Conteúdo |
|---|---|---|
| Bronze | JSON | Dados extraídos da API |
| Silver | Parquet | Dados limpos e estruturados |
| Gold | Parquet | Agregações e rankings analíticos |

Os arquivos Gold permitem realizar consultas e análises sobre os atributos dos Pokémon sem precisar consumir novamente a API.

## Aprendizados

Este projeto explora conceitos fundamentais de Engenharia de Dados:

- Consumo de APIs REST e paginação.
- Organização de pipelines ETL.
- Separação entre extração, transformação e carregamento.
- Modelagem e tratamento de dados semiestruturados.
- Manipulação de dados com Pandas.
- Armazenamento colunar com Parquet.
- Organização de código Python em módulos.
- Versionamento de projetos e gerenciamento de dependências.

## Próximas melhorias

- Implementar logging estruturado e tratamento de falhas.
- Adicionar testes automatizados para as transformações.
- Evitar chamadas desnecessárias à API em execuções posteriores.
- Implementar atualização incremental dos dados.
- Orquestrar o pipeline com Apache Airflow.
- Avaliar o uso de bancos de dados para persistência dos resultados.
- Adicionar documentação e exemplos de consultas aos dados Gold.

## Fonte dos dados

Os dados são obtidos da [PokeAPI](https://pokeapi.co/), uma API pública sobre Pokémon.

---

Projeto desenvolvido para fins de estudo e portfólio em Engenharia de Dados.
