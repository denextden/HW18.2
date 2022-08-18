from flask_restx import Resource, Namespace

from dao.model.movies import MoviesSchema
from implemented import movies_service

movies_ns = Namespace('movies')


@movies_ns.route('/')
class MoviesView(Resource):
    def get(self):
        movies = movies_service.get_all()
        result = MoviesSchema(many=True).dump(movies)
        return result, 200

    # def post(self):
    #     return "", 201
