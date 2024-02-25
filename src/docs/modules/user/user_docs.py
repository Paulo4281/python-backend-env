from flask_restx import Namespace, Resource
from src.modules.user.models.user_model import UserModel

api = Namespace("User")

user_model = UserModel(api)

@api.route("/auth")
class UserResourceAuth(Resource):
    @api.expect(user_model.auth())
    @api.marshal_with(fields=user_model.auth_response())
    @staticmethod
    def post() -> None:
        pass

@api.route("/")
class UserResource(Resource):
    @api.expect(user_model.save())
    @api.marshal_with(fields=user_model.find(), description="Created", code=201)
    @staticmethod
    def post() -> None:
        pass

    @api.marshal_with(fields=user_model.find(), as_list=True)
    @staticmethod
    def get() -> None:
        pass

@api.route("/<id_>")
class UserResourceDetail(Resource):
    @api.marshal_with(fields=user_model.find_by_id())
    @staticmethod
    def get() -> None:
        pass

    @api.expect(user_model.update())
    @api.marshal_with(fields=None, description="No Content", code=204)
    @staticmethod
    def put() -> None:
        pass

    @api.marshal_with(fields=None, description="No Content", code=204)
    @staticmethod
    def delete() -> None:
        pass