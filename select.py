import pymssql

conn = pymssql.connect(host=r'127.0.0.1', user=r'sa',
                       password=r'6HJaDCj5mK65nzu8', database=r'mydb')
cur = conn.cursor()
cur.execute(r'SELECT * FROM users')
row = cur.fetchone()
print(row)
cur.close()
conn.close()
