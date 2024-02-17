from src.routes.index_routes import book_routes
from src.utils.http_response import HttpResponse
from src.modules.book.controllers.book_controller import BookController
from flask_cors import cross_origin

@book_routes.route("/", methods=["POST"])
@cross_origin()
def save() -> HttpResponse:
    return BookController.save()

@book_routes.route("", methods=["GET"])
@cross_origin()
def find() -> HttpResponse:
    return BookController.find()