""" comandos para inserir dados
insert_one() e insert_many()
"""
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
print(client.list_database_names())

db = client.Estudo_MongoDB

db.insert_one()