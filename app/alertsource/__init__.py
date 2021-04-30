from flask import Blueprint
from flask_restful import Api
from resources.store import Store

alertsource = Blueprint("alertsource", __name__, url_prefix="/alertsource")
api = Api(alertsource)

api.add_resource(Store, "/store/<string:name>")