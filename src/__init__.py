from flask import Flask
from src.database import db


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:

        app.config.from_mapping(
            SECRET_KEY="dev",
            SQLALCHEMY_DATABASE_URI="sqlite:///bookmarks.db"

        )
    else:
        app.config.from_mapping(test_config)

    @app.get('/')
    def home():
        return "Home"

    @app.get('/hello')
    def hello():
        return {'message': 'Hello'}

    db.app = app
    db.init_app(app)

    return app
