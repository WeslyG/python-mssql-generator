#!/usr/bin/python
# coding: utf-8

import pymssql
import generate

users = generate.get_users(1000)

conn = pymssql.connect(host=r'127.0.0.1', user=r'sa',
              password=r'6HJaDCj5mK65nzu8', database=r'mydb')
cur = conn.cursor()

cur.execute("""
CREATE TABLE users (
    id INT NOT NULL,
    first_name NVARCHAR(100),
    last_name NVARCHAR(100),
    age INT,
    gender NVARCHAR(1),
    location NVARCHAR(100),
    PRIMARY KEY(id)
)
""")

cur.executemany(
    "INSERT INTO users VALUES (%d, %s, %s, %d, %s, %s)", users)

conn.commit()


cur.close()
conn.close()
