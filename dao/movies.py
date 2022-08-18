from dao.model.movies import Movies, MoviesSchema


class MoviesDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        movies = Movies.query.all()
        return movies
