from src.routes.index_routes import review_routes
from src.utils.http_response import HttpResponse
from src.modules.book.controllers.review_controller import ReviewController
from flask_cors import cross_origin
from flask_jwt_extended import jwt_required

@review_routes.route("/", methods=["POST"])
@jwt_required()
@cross_origin()
def save() -> HttpResponse:
    return ReviewController.save()

@review_routes.route("/", methods=["GET"])
@jwt_required()
@cross_origin()
def find() -> HttpResponse:
    return ReviewController().find()

@review_routes.route("/<id_>", methods=["GET"])
@jwt_required()
@cross_origin()
def find_by_id(id_: str) -> HttpResponse:
    return ReviewController().find_by_id(id_)

@review_routes.route("/<id_>", methods=["PUT"])
@jwt_required()
@cross_origin()
def update(id_: str) -> HttpResponse:
    return ReviewController().update(id_)

@review_routes.route("/<id_>", methods=["DELETE"])
@jwt_required()
@cross_origin()
def delete(id_: str) -> HttpResponse:
    return ReviewController.delete(id_)