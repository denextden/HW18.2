from flask_restx import Resource, Namespace

from dao.model.genres import GenresSchema
from implemented import genres_service

genres_ns = Namespace('genres')


@genres_ns.route('/')
class GenresView(Resource):
    def get(self):
        genres = genres_service.get_all()
        result = GenresSchema(many=True).dump(genres)

        return result, 200


@genres_ns.route('/<int:gid>')
class GenresView(Resource):
    def get(self, gid):
        genres = genres_service.get_one(gid)
        result = GenresSchema().dump(genres)

        return result, 200
