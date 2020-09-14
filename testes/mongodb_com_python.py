from pymongo import MongoClient
client = MongoClient('localhost', 27017)
print(client.list_database_names())

# Cliente base de dados
db = client.Estudo_MongoDB

# Inserindo dados
"""db.teste.insert_many(
    [
        {'id': 1},
        {'id': 12},
        {'id': 500},
        {'id': -222}
    ]
)"""
db.teste.insert_one(
    {'bala': 'Ze do amendoin'}
)
