from dynaconf import FlaskDynaconf
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app =  Flask(__name__)
    FlaskDynaconf(app)
    app.config.load_extensions()
    
    db.init_app(app)
    Migrate(app, db)

    from app import routes
    routes.init_app(app)

    return app
