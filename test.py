#!/usr/bin/python
# coding: utf-8

from sqlalchemy import Table, MetaData, Column, Integer, String, create_engine
# import pymssql
# import generate
# users = generate.get_users(1)
# print(users)

engine = create_engine(
    'mssql+pymssql://sa:6HJaDCj5mK65nzu8@127.0.0.1:1433/mydb?charset=utf8',
    encoding='utf8')

metadata = MetaData()
test = Table('test', metadata, Column('id', Integer, primary_key=True),
        Column('name', String), Column('fullname', String))
metadata.create_all(engine)

ins = test.insert().values(name='Юрий', fullname='Гагарин')
conn = engine.connect()
result = conn.execute(ins)
