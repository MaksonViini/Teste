from pymongo import MongoClient

uri = 'mongodb://root:example@localhost:27017/'

client = MongoClient(uri)

database = client['users']
collection = database['user']


def insert(**args):
    collection.insert(args)


def read(**args):
    return collection.find(args)


def read_one(**args):
    return collection.find_one(args)


def update(**args):
    collection.update(args)


def delete(**args):
    collection.delete(args)
