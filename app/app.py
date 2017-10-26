from flask import Flask, make_response
import graphene
from flask_graphql import GraphQLView
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()

from .config import Config
from .schema import schema


def create_app(config_object=Config):
    app = Flask(__name__)
    app.debug = True
    app.config.from_object(config_object)
    db.init_app(app)
    migrate.init_app(app, db)
    app.add_url_rule(
        '/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))
    return app
