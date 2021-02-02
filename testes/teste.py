from pymongo import MongoClient
client = MongoClient('localhost', 27017)
print(client.list_database_names())
titulo = str(input('Digite um titulo: '))
db = client.Estudo_MongoDB