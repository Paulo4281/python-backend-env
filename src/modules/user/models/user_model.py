from flask_restx import fields, Namespace
from typing import Any

class UserModel:
    def __init__(self, namespace: Namespace) -> None:
        self.namespace = namespace

    def auth(self) -> Any:
        data_model = {
            "mail": fields.String(),
            "password": fields.String()
        }
        return self.namespace.model("user_auth", data_model)
    
    def auth_response(self) -> Any:
        data_model = {
            "token": fields.String()
        }
        return self.namespace.model("user_auth_response", data_model)

    def save(self) -> Any:
        data_model = {
            "name": fields.String(),
            "mail": fields.String(),
            "password": fields.String(),
            "birth": fields.Date()
        }
        return self.namespace.model("user_save", data_model)

    def find(self) -> Any:
        return self.namespace.model("user_find", self.find_by_id())

    def find_by_id(self) -> Any:
        data_model = {
            "id_": fields.String(),
            "name": fields.String(),
            "mail": fields.String(),
            "birth": fields.Date(),
            "created_at": fields.DateTime()
        }
        return self.namespace.model("user_find_by_id", data_model)
    
    def update(self) -> Any:
        return self.namespace.model("user_update", self.save())