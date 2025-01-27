from flask import Flask
from .config.env import EnvConfig
from .sqlite.database import db, migrate
from .routes import register_routes


def create_app():
    app = Flask(__name__)
    app.config.from_object(EnvConfig)

    db.init_app(app)
    migrate.init_app(app, db)

    register_routes(app)

    return app
