from src.routes.index_routes import user_routes
from src.modules.user.controllers.user_controller import UserController
from flask import Response

@user_routes.route("/auth", methods=["POST"])
def auth() -> Response:
    return UserController.auth()

@user_routes.route("/", methods=["POST"])
def save() -> Response:
    return UserController.save()