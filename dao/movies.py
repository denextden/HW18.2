from dao.model.movies import Movies


class MoviesDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        movies = Movies.query.all()
        return movies

    def get_one(self, mid):
        movie = Movies.query.get(mid)
        return movie

    def create(self, data):
        movie = Movies(**data)
        self.session.add(movie)
        self.session.commit()
        self.session.close()
