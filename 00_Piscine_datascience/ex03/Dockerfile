FROM postgres:latest

RUN apt-get update && apt-get install -y python3 python3-pip

COPY automatic_table.py /docker-entrypoint-initdb.d/automatic_table.py
COPY ../customer /docker-entrypoint-initdb.d/customer