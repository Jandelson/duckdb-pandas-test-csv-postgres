# duckdb-pandas-test-csv-postgres

### Importação de dados csv para PostgresSQL

#### *Este teste pode abranger diversos cenários, mas não tem o objetivo de julgar ou determinar qual ferramenta ou tecnologia é superior, pois ambas podem se complementar.*

<hr>

### Fluxo do teste
<hr>

### Executar o arquivo compose.yml com docker ou podman
Criação do banco de dados postgres
```
podman compose up -d
```

### Criação do ambiente python
```
python3 -m venv duckdb

source duckdb/bin/active

pip install -r requirements.txt
```

### Gerar arquivo para o teste
Executar arquivo 60M.py para gerar um arquivo csv do teste, o arquivo gerado vai ter 771MB com 60 milhões de linhas
```
python3 60M.py
```

### Executar teste pandas
```
python3 teste_pandas.py
```

### Executar teste duckdb
```
python3 teste_duckdv.py
```

### Resultados do meu teste:
#### Ambiente do teste
- Windows wsl2
- Processador: I7
- Memória 32GB


### Código

```python
python3 teste_pandas.py
Killed

python3 teste_duckdb.py

Tabela 'dataset_duckdb' criada e dados inseridos no PostgreSQL! 86.44 segundos.

podman exec -it postgres /bin/bash

psql -U usuario -W password -d banco_de_dados

\c banco_de_dados

select count(*) from dataset_duckdb

  count
----------
 60000000
(1 row)
```

O script com Pandas consumiu muita memória e foi encerrado.

O DuckDB foi mais eficiente para carregar os dados e inseri-los no PostgreSQL, concluindo o processo em 86,44 segundos.

A tabela dataset_duckdb foi corretamente criada e preenchida com 60 milhões de registros no PostgreSQL.
