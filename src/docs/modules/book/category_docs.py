from flask_restx import Namespace, Resource
from src.modules.book.models.category_model import CategoryModel

api = Namespace("Category")

category_model = CategoryModel(api)

@api.route("/")
class CategoryResource(Resource):

    @api.marshal_with(category_model.find(), as_list=True)
    @staticmethod
    def get():
        pass