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