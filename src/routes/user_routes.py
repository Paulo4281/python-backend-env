from src.routes.index_routes import user_routes
from src.modules.user.controllers.user_controller import UserController
from src.utils.http_response import HttpResponse
from flask_cors import cross_origin
from flask_jwt_extended import jwt_required

@user_routes.route("/auth", methods=["POST"])
@cross_origin()
def auth() -> HttpResponse:
    return UserController.auth()

@user_routes.route("/", methods=["POST"])
@jwt_required()
@cross_origin()
def save() -> HttpResponse:
    return UserController.save()

@user_routes.route("/", methods=["GET"])
@jwt_required()
@cross_origin()
def find() -> HttpResponse:
    return UserController.find()

@user_routes.route("/<id_>", methods=["GET"])
@jwt_required()
@cross_origin()
def find_by_id(id_: str) -> HttpResponse:
    return UserController.find_by_id(id_)

@user_routes.route("/<id_>", methods=["PUT"])
@jwt_required()
@cross_origin()
def update(id_: str) -> HttpResponse:
    return UserController.update(id_)

@user_routes.route("/<id_>", methods=["DELETE"])
@jwt_required()
@cross_origin()
def delete(id_: str) -> HttpResponse:
    return UserController.delete(id_)