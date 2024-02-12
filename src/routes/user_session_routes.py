from src.routes.index_routes import user_session_routes
from src.modules.user_session.controllers.user_session_controller import UserSessionController
from flask import Response

@user_session_routes.route("/", methods=["POST"])
def auth() -> Response:
    return UserSessionController.auth()