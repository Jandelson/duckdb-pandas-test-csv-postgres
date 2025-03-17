import duckdb
import time

start_time = time.time()

POSTGRES_CONN = "postgresql://user:password@localhost:5432/database"

file = "large_dataset.csv"
table_name = "dataset_duckdb"

conn = duckdb.connect("database.duckdb")

# Os comandos abaixo são utilizados para instalar e habilitar a extensão do postgres no duckdb
conn.execute("INSTALL postgres;")
conn.execute("LOAD postgres;")

# Adiciona a conexão do postgres no duckdb
conn.execute(f"ATTACH '{POSTGRES_CONN}' AS postgres (TYPE POSTGRES);")

# Cria a tabela no duckdb com os dados carregados
# O duckdb tem outras opções de importação para arquivos xlsx e parquet além do csv
conn.execute(f"CREATE OR REPLACE TABLE {table_name} AS SELECT * FROM read_csv_auto('{file}');")

conn.execute(f"""
    CREATE TABLE IF NOT EXISTS postgres.public.{table_name} AS
    SELECT * FROM {table_name}
""")

conn.execute(f"""
    INSERT INTO postgres.public.{table_name}
    SELECT * FROM {table_name}
""")

end_time = time.time()

print(f"Tabela '{table_name}' criada e dados inseridos no PostgreSQL! {end_time - start_time:.2f} segundos.")

conn.close()
