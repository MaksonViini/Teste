from pymongo import MongoClient
client = MongoClient('localhost', 27017)
print(client.list_database_names())
titulo = str(input('Digite um titulo: '))
db = client.Estudo_MongoDB



db.createCollection({   
    Title: {
        type: String,
    },
    Sub_Title: {
        type: String
    },
    Peoples: {
        type: String,
        Id: {
            type: String, 
            Nome: String,
            Cargo: String,
            Imagem: String,
            Twitter: String,
            Facebook: String,
            Gmail: String,
            linkedin: String,
            unique: true

        }
    }             
});
