#!/usr/bin/python
# coding: cp1251
import pymssql

conn = pymssql.connect(host=r'127.0.0.1', user=r'sa',
              password=r'6HJaDCj5mK65nzu8', database=r'mydb')
cur = conn.cursor()

cur.execute("""
CREATE TABLE users (
    id INT NOT NULL,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    age INT,
    gender VARCHAR(1),
    location VARCHAR(100),
    buy_list INT,
    PRIMARY KEY(id)
)
""")

cur.executemany(
    "INSERT INTO users VALUES (%d, %s, %s, %d, %s, %s, %d)",
    [(1, 'Вова', 'Лила', 19, 'F', 'Russia', 0),
     (2, 'Тест', 'Кошелева', 19, 'F', 'Russia', 12)])

conn.commit()

cur.close()
conn.close()
