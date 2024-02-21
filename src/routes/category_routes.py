from src.routes.index_routes import category_routes
from src.utils.http_response import HttpResponse
from src.modules.book.controllers.category_controller import CategoryController
from src.modules.book.models.category_model import CategoryModel
from flask_restx import Namespace, Resource
from flask_cors import cross_origin

api = Namespace("Category", "")
category_model = CategoryModel(api)

@api.route("/")
class CategoryResource(Resource):

    @api.marshal_with(category_model.find())
    @category_routes.route("/", methods=["GET"])
    def get(self) -> HttpResponse:
        return CategoryController.find()
    
    # @category_routes.route("/", methods=["POST"])
    # @cross_origin()
    # def save() -> HttpResponse:
    #     return CategoryController.save()


    # @category_routes.route("/<id_>", methods=["GET"])
    # @cross_origin()
    # def find_by_id(id_: str) -> HttpResponse:
    #     return CategoryController.find_by_id(id_)

    # @category_routes.route("/<id_>", methods=["PATCH"])
    # @cross_origin()
    # def update(id_: str) -> HttpResponse:
    #     return CategoryController.update(id_)

    # @category_routes.route("/<id_>", methods=["DELETE"])
    # @cross_origin()
    # def delete(id_: str) -> HttpResponse:
    #     return CategoryController.delete(id_)