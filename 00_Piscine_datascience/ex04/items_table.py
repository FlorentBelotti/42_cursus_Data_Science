import os
import pandas as pd

CSV_FILE = "/docker-entrypoint-initdb.d/item.csv"
OUTPUT_SQL = "/docker-entrypoint-initdb.d/init.sql"

print("[items_table.py]: Creating SQL file...")

if os.path.exists(OUTPUT_SQL):
    os.remove(OUTPUT_SQL)

df = pd.read_csv(CSV_FILE)

column_types = {
    "product_id": "INTEGER",
    "category_id": "BIGINT",
    "category_code": "VARCHAR(100)",
    "brand": "VARCHAR(100)"
}

with open(OUTPUT_SQL, "a") as f:
    print("[items_table.py]: Creating table for item.csv")

    f.write("CREATE TABLE items (\n")

    for i, column in enumerate(df.columns):
        column_type = column_types.get(column, 'VARCHAR(100)')
        if i < len(df.columns) - 1:
            f.write(f"  {column} {column_type},\n")
        else:
            f.write(f"  {column} {column_type}\n")
    f.write(");\n")

    columns = ', '.join(df.columns)
    f.write("COPY items ({columns})\n")
    f.write("FROM '/docker-entrypoint-initdb.d/item.csv'\n")
    f.write("DELIMITER ','\n")
    f.write("CSV HEADER;\n\n")

print("[items_table.py]: Script finished")
