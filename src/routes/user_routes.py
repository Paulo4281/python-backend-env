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

@user_routes.route("/<id>", methods=["GET"])
@cross_origin()
def find_by_id(id: str) -> HttpResponse:
    return UserController.find_by_id(id)

@user_routes.route("/<id>", methods=["PATCH"])
@cross_origin()
def update(id: str) -> HttpResponse:
    return UserController.update(id)

@user_routes.route("/<id>", methods=["DELETE"])
@cross_origin()
def delete(id: str) -> HttpResponse:
    return UserController.delete(id)