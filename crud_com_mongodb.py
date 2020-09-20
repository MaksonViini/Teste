from pymongo import MongoClient
client = MongoClient('localhost', 27017)
print(client.list_database_names())
titulo = str(input('Digite um titulo: '))
db = client.Estudo_MongoDB

db.banco.insert_one(
    {
    'Title': {
        'Titulo': titulo,
    },
    'Sub_Title': {
        'type': 'String'
    },
    'Peoples': {
        'Id': {
            'type': 'String', 
            'Nome': 'String',
            'Cargo': 'String',
            'Imagem': 'http/smdskdksd',
            'Twitter': 'twitter.com',
            'Facebook': 'fb.cmo',
            'Gmail': 'gmail.com',
            'linkedin': 'linkedin.com',
            'unique': 'true'

        }
    } 
    }
) 
