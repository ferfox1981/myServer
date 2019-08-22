from flask import Flask
from flask_restful import Api
from moviesDAO import MoviesDAO


app = Flask(__name__)
api = Api(app)

api.add_resource(MoviesDAO, "/certain-movie/<string:name>")

app.run()
