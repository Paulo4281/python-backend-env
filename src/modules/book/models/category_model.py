from flask_restx import fields

class CategoryModel:
    def __init__(self, namespace):
        self.namespace = namespace

    def save(self):
        data_model = {
            "name": fields.String()
        }
        return self.namespace.model("save", data_model)

    def find(self):
        return self.namespace.model("find", self.find_by_id())

    def find_by_id(self):
        data_model = {
            "id": fields.String(),
            "name": fields.String(),
            "created_at": fields.DateTime()
        }
        return self.namespace.model("find_by_id", data_model)
    
    def update(self):
        return self.namespace.model("update", self.save())