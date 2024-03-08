from src.routes.index_routes import view_routes
from src.modules.views.controllers.views_controller import ViewController
from flask_cors import cross_origin
from flask_jwt_extended import jwt_required
from flask import Response

@view_routes.route("/verify", methods=["POST"])
@cross_origin()
def verify() -> Response:
    return ViewController().verify()

@view_routes.route("/", methods=["GET"])
@cross_origin()
def index() -> str:
    return ViewController().index()

@view_routes.route("/dash", methods=["GET"])
@cross_origin()
def dash() -> str:
    return ViewController().dash()