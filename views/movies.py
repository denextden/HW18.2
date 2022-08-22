from flask import request, jsonify
from flask_restx import Resource, Namespace

from dao.model.movies import MoviesSchema
from implemented import movies_service

movies_ns = Namespace('movies')


@movies_ns.route('/')
class MoviesView(Resource):
    def get(self):
        year = request.args.get('year')
        genre_id = request.args.get('genre_id')
        director_id = request.args.get('director_id')

        if year:
            movies = movies_service.get_by_year(year)
        elif genre_id:
            movies = movies_service.get_by_genre(genre_id)
        elif director_id:
            movies = movies_service.get_by_director(director_id)
        else:
            movies = movies_service.get_all()

        result = MoviesSchema(many=True).dump(movies)
        return result, 200

    def post(self):
        data = request.get_json()
        movies_id = data['id']
        movies_service.create(data)
        response = jsonify()
        response.status_code = 201
        response.headers['location'] = f'movies/{movies_id}'
        return "", 201


@movies_ns.route('/<int:mid>')
class MoviesView(Resource):
    def get(self, mid):
        movie = movies_service.get_one(mid)
        result = MoviesSchema().dump(movie)
        return result, 200

    def put(self, mid):
        data = request.get_json()
        movies_service.update(data, mid)

        return '', 204

    def patch(self, mid):
        data = request.get_json()
        movies_service.update_part(data, mid)

        return '', 204

    def delete(self, mid):
        movies_service.delete(mid)

        return '', 204
