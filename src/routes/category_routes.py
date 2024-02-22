from src.routes.index_routes import category_routes
from src.utils.http_response import HttpResponse
from src.modules.book.controllers.category_controller import CategoryController
from flask_cors import cross_origin

@category_routes.route("/", methods=["POST"])
@cross_origin()
def save() -> HttpResponse:
    return CategoryController.save()

@category_routes.route("/", methods=["GET"])
@cross_origin()
def find() -> HttpResponse:
    return CategoryController.find()

@category_routes.route("/<id_>", methods=["GET"])
@cross_origin()
def find_by_id(id_: str) -> HttpResponse:
    return CategoryController.find_by_id(id_)

@category_routes.route("/<id_>", methods=["PUT"])
@cross_origin()
def update(id_: str) -> HttpResponse:
    return CategoryController.update(id_)

@category_routes.route("/<id_>", methods=["DELETE"])
@cross_origin()
def delete(id_: str) -> HttpResponse:
    return CategoryController.delete(id_)