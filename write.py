#!/usr/bin/python
# coding: cp1251
import pymssql

conn = pymssql.connect(host=r'127.0.0.1', user=r'sa',
              password=r'6HJaDCj5mK65nzu8', database=r'mydb')
cur = conn.cursor()

cur.execute("""
CREATE TABLE users (
    id INT NOT NULL,
    first_name NVARCHAR(100),
    last_name NVARCHAR(100),
    gender NVARCHAR(1),
    location NVARCHAR(100),
    buy_list INT,
    PRIMARY KEY(id)
)
""")

cur.executemany(
    "INSERT INTO users VALUES (%d, %s, %s, %d, %s, %s, %d)",
    [(1, 'фыв', 'йцу', 19, 'F', 'Russia', 0),
     (2, 'чсм', 'яччс', 19, 'F', 'Russia', 12)])

conn.commit()

cur.close()
conn.close()
