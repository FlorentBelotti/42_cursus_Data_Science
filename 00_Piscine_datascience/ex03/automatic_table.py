import os
import pandas as pd

CSV_DIR = "/docker-entrypoint-initdb.d/customer"
OUTPUT_SQL = "/docker-entrypoint-initdb.d/init.sql"

print("[automatic_table.py]: Creating SQL file...")

if os.path.exists(OUTPUT_SQL):
    os.remove(OUTPUT_SQL)

for csv_file in os.listdir(CSV_DIR):

    if csv_file.endswith(".csv"):

        # Table name
        table_name = os.path.splitext(csv_file)[0]

        print(f'"[automatic_table.py]: creating table <{table_name}>..."')

        # Read CSV
        current_csv = pd.read_csv(os.path.join(CSV_DIR, csv_file))

        print(f'"[automatic_table.py]: <{table_name}.csv> opened..."')

        # Set column types
        column_types = {
            "timestamp": "TIMESTAMP",
            "customer_id": "INTEGER",
            "name": "VARCHAR(100)",
            "email": "VARCHAR(100)",
            "age": "INTEGER",
            "balance": "NUMERIC",
            "is_active": "BOOLEAN"
        }

        # Add SQL commands
        with open(OUTPUT_SQL, "a") as f:

            print(f'"[automatic_table.py]: <{table_name}.csv> creatin..."')

            # Specify name
            f.write(f"CREATE TABLE {table_name} (\n")

            # Specify columns
            for column in current_csv.columns:
                f.write(f"  {column} {column_types.get(column, 'VARCHAR(100)')},\n")
            f.write(");\n")

            # Create SQL command to import data
            f.write(f"COPY {table_name} ({', '.join(current_csv.columns)})\n")
            f.write(f"FROM '/docker-entrypoint-initdb.d/customer/{csv_file}'\n")
            f.write("DELIMITER ','\n")
            f.write("CSV HEADER;\n\n")
