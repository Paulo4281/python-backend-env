from flask_restx import fields

class CategoryModel:
    def __init__(self, namespace):
        self.namespace = namespace

    def find(self):
        return self.namespace.model("find", self.find_by_id())

    def find_by_id(self):
        data_model = {
            "id": fields.String(),
            "name": fields.String(),
            "created_at": fields.DateTime()
        }
        return self.namespace.model("find_by_id", data_model)