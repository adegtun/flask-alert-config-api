from flask_restful import Resource


NAME_ALREADY_EXISTS = "A store with name '{}' already exists."
ERROR_INSERTING = "An error occurred while inserting the store."
STORE_NOT_FOUND = "Store not found."
STORE_DELETED = "Store deleted."

#store_schema = StoreSchema()
#store_list_schema = StoreSchema(many=True)


class Store(Resource):
    @classmethod
    def get(cls, name: str):
        return "Hello, {} package!".format(name)

