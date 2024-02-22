from flask_restx import Namespace, Resource
from src.modules.book.models.book_model import BookModel

api = Namespace("Book")

book_model = BookModel(api)

@api.route("/")
class BookResource(Resource):
    @api.expect(book_model.save())
    @api.marshal_with(book_model.find(), description="Created", code=201)
    @staticmethod
    def post() -> None:
        pass

    @api.marshal_with(book_model.find(), as_list=True)
    @staticmethod
    def get() -> None:
        pass