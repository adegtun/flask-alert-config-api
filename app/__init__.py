# app/__init__.py
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(config_type): # dev, test, prod
    app = Flask(__name__)
    configuration = os.path.join(os.getcwd(), 'config', config_type+'.py')
    app.config.from_pyfile(configuration)

    db.init_app(app)

    from app.alertsource import alertsource
    from app.datasource import datasource
    app.register_blueprint(alertsource)
    app.register_blueprint(datasource)

    return app
