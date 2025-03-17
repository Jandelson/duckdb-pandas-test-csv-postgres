import pandas as pd
from sqlalchemy import create_engine

import time

start_time = time.time()

POSTGRES_URL = "postgresql://user:password@localhost:5432/database"

file = "large_dataset.csv"
table_name = "databaset"

df = pd.read_csv(file)

engine = create_engine(POSTGRES_URL)

df.to_sql(table_name, engine, if_exists="replace", index=False)

end_time = time.time()

print(f"Tabela '{table_name}' criada e dados inseridos no PostgreSQL! {end_time - start_time:.2f} segundos.")