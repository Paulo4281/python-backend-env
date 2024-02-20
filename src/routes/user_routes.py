from src.routes.index_routes import user_routes
from src.modules.user.controllers.user_controller import UserController
from src.utils.http_response import HttpResponse
from flask_cors import cross_origin

@user_routes.route("/auth", methods=["POST"])
@cross_origin()
def auth() -> HttpResponse:
    return UserController.auth()

@user_routes.route("/", methods=["POST"])
@cross_origin()
def save() -> HttpResponse:
    return UserController.save()

@user_routes.route("/", methods=["GET"])
@cross_origin()
def find() -> HttpResponse:
    return UserController.find()

@user_routes.route("/<id_>", methods=["GET"])
@cross_origin()
def find_by_id(id_: str) -> HttpResponse:
    return UserController.find_by_id(id_)

@user_routes.route("/<id_>", methods=["PATCH"])
@cross_origin()
def update(id_: str) -> HttpResponse:
    return UserController.update(id_)

@user_routes.route("/<id_>", methods=["DELETE"])
@cross_origin()
def delete(id_: str) -> HttpResponse:
    return UserController.delete(id_)