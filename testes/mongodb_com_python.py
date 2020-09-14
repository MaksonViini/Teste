from pymongo import MongoClient
client = MongoClient('localhost', 27017)
print(client.list_database_names())

# Cliente basse de dados
db = client.Estudo_MongoDB

# Inserindo dados
db.teste.insert_many(
    
)
