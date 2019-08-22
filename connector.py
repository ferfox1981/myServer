import pymongo


def get_connection(user, password):
    client = pymongo.MongoClient(
        f'mongodb+srv://{user}:{password}@cluster0-iyq1g.mongodb.net/test?retryWrites=true&w=majority')
    return client

