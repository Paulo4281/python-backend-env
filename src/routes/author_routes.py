from src.routes.index_routes import author_routes
from src.utils.http_response import HttpResponse
from src.modules.book.controllers.author_controller import AuthorController
from flask_cors import cross_origin
from flask_jwt_extended import jwt_required

@author_routes.route("/", methods=["POST"])
@jwt_required()
@cross_origin()
def save() -> HttpResponse:
    return AuthorController.save()

@author_routes.route("/", methods=["GET"])
@jwt_required()
@cross_origin()
def find() -> HttpResponse:
    return AuthorController.find()