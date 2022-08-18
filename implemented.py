from dao.movies import MoviesDAO
from service.movies import MoviesService
from setup_db import db

movies_dao = MoviesDAO(db.session)
movies_service = MoviesService(movies_dao=movies_dao)
#
# review_dao = ReviewDAO(db.session)
# review_service = ReviewService(dao=review_dao)
