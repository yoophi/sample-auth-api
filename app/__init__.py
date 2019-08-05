from flask import Flask

from app.api import api as api_bp
from app.auth import auth as auth_bp
from app.config import config
from app.extensions import cors, ma, jwt
from app.main import main as main_bp
from app.repository.sqla.database import db
from app.swagger import swagger_bp


def init_blueprint(app):
    app.register_blueprint(main_bp)
    app.register_blueprint(api_bp, url_prefix="/api")
    app.register_blueprint(auth_bp, url_prefix="/auth")

    if app.config['EXPOSE_SWAGGER_ROUTES']:
        app.register_blueprint(swagger_bp, url_prefix="/swagger")


def init_extensions(app):
    if app.config['REPOSITORY'] == "MYSQL":
        db.init_app(app)

    cors.init_app(app)
    ma.init_app(app)
    jwt.init_app(app)


def create_app(config_name="default"):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    init_extensions(app)
    init_blueprint(app)

    return app
