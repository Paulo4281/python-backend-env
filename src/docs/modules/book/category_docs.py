from flask_restx import Namespace, Resource
from src.modules.book.models.category_model import CategoryModel
from src.utils.app_docs_auth import authorizations

api = Namespace("Category", authorizations=authorizations)
category_model = CategoryModel(api)

@api.doc(security="jsonwebtoken")
@api.route("/")
class CategoryResource(Resource):
    @api.expect(category_model.save())
    @api.marshal_with(fields=category_model.find(), description="Created", code=201)
    @staticmethod
    def post() -> None:
        pass

    @api.marshal_with(fields=category_model.find(), as_list=True)
    @staticmethod
    def get() -> None:
        pass

@api.doc(security="jsonwebtoken")
@api.route("/<id_>")
class CategoryResourceDetail(Resource):
    @api.marshal_with(fields=category_model.find_by_id())
    @staticmethod
    def get() -> None:
        pass

    @api.expect(category_model.update())
    @api.marshal_with(fields=None, description="No Content", code=204)
    @staticmethod
    def put() -> None:
        pass

    @staticmethod
    @api.marshal_with(fields=None, description="No Content", code=204)
    def delete() -> None:
        pass