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


""" comandos para inserir dados
insert_one() e insert_many()
"""
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
print(client.list_database_names())

db = client.Estudo_MongoDB

""" db.pessoas.insert_one(
    {
        'id': 1,
        'Nome': 'Makson', 
        'idade': 20
    }
) """

"""db.pessoas.insert_one(
    {
        'id': 1,
        'Nome': 'Aderbardo', 
        'idade': 50, 
        'filhos': ['Jr', 'Caboclo', 'Raules']

    }
) """

db.pessoas.insert_many(
    [
        {
        'id': 1,
        'Nome': 'Aderbardo'
        }, 
        {
        'id': 2,
        'Nome': 'Canhoto'
        }, 
        {
        'id': 3,
        'Nome': 'Geraldao'
        }
    ]
)