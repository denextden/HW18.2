from flask import Flask
from flask_restx import Api
from config import Config
from setup_db import db
from views.movies import movies_ns


# from models import Review, Book
# from setup_db import db
# from views.books import book_ns
# from views.reviews import review_ns
#
# функция создания основного объекта app


def create_app(config_object):
    application = Flask(__name__)
    application.config.from_object(config_object)
    register_extensions(application)
    return application


# функция подключения расширений (Flask-SQLAlchemy, Flask-RESTx, ...)
def register_extensions(application):
    db.init_app(application)
    api = Api(application)
    api.add_namespace(movies_ns)


if __name__ == '__main__':
    app_config = Config()
    app = create_app(app_config)
    app.run()
