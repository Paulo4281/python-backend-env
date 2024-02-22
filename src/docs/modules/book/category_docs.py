from flask_restx import Namespace, Resource
from src.modules.book.models.category_model import CategoryModel

api = Namespace("Category")

category_model = CategoryModel(api)

@api.route("/")
class CategoryResource(Resource):
    @api.expect(category_model.save())
    @api.marshal_with(category_model.find(), description="Created", code=201)
    @staticmethod
    def post():
        pass

    @api.marshal_with(category_model.find(), as_list=True)
    @staticmethod
    def get():
        pass

@api.route("/<id_>")
class CategoryResource(Resource):
    @api.marshal_with(category_model.find_by_id())
    @staticmethod
    def get():
        pass

    @api.expect(category_model.update())
    @staticmethod
    def put():
        pass

    @staticmethod
    def delete():
        pass