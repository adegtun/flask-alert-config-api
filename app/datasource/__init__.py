from flask import Blueprint
from flask_restful import Api
from resources.store import Store

datasource = Blueprint("datasource", __name__, url_prefix="/datasource")
api = Api(datasource)

api.add_resource(Store, "/store/<string:name>")