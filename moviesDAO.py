
from connector import get_connection
from flask_restful import Resource, reqparse
from bson.json_util import dumps



conn = get_connection('xxx', 'yyyyy')
colection = conn['sample_mflix']['movies']


class MoviesDAO(Resource):

    def get(self,name):
        myquery = {'title':name}
        mydoc = colection.find_one(myquery)
        if mydoc is not None:
            return mydoc['title'], 200
        return 'Movie Not Found', 404

    def post(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument('word')
        args = parser.parse_args()
        myquery = {'title':{'$regex':args['word']}}
        mydoc = colection.find(myquery)
        return dumps(mydoc)
