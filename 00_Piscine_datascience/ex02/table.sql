CREATE TABLE data_2022_oct (
  event_time TIMESTAMP,
  event_type VARCHAR(100),
  product_id INTEGER,
  price NUMERIC,
  user_id INTEGER,
  user_session VARCHAR(100)
);

COPY data_2022_oct (event_time, event_type, product_id, price, user_id, user_session)
FROM '/docker-entrypoint-initdb.d/data_2022_oct.csv'
DELIMITER ','
CSV HEADER;