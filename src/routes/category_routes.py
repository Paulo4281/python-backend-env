from src.routes.index_routes import category_routes
from src.utils.http_response import HttpResponse
from src.modules.book.controllers.category_controller import CategoryController
from flask_cors import cross_origin

@category_routes.route("/", methods=["POST"])
@cross_origin()
def save() -> HttpResponse:
    return CategoryController.save()