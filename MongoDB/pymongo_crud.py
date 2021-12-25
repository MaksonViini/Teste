from pymongo import MongoClient

uri = 'mongodb://root:example@localhost:27017/'

client = MongoClient(uri)

database = client['users']
collection = database['user']


def insert(**args):
    collection.insert(args)


def read(**args):
    return collection.find(args)


def read_for_age(age):
    return collection.find({'age': age})


def read_for_age_with_operator(op, age):
    return collection.find({'age': {op: age}})


def update(args):
    collection.update(args[0], args[1])


def delete(args):
    collection.remove(args)
