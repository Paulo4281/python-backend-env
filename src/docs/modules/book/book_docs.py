from flask_restx import Namespace, Resource
from src.modules.book.models.book_model import BookModel
from src.utils.app_docs_auth import authorizations

api = Namespace("Book", authorizations=authorizations)
book_model = BookModel(api)

@api.doc(security="jsonwebtoken")
@api.route("/")
class BookResource(Resource):
    @api.expect(book_model.save())
    @api.marshal_with(fields=book_model.find(), description="Created", code=201)
    @staticmethod
    def post() -> None:
        pass

    @api.marshal_with(fields=book_model.find(), as_list=True)
    @staticmethod
    def get() -> None:
        pass

@api.doc(security="jsonwebtoken")
@api.route("/<id_>")
class BookResourceDetail(Resource):
    @api.marshal_with(fields=book_model.find_by_id())
    @staticmethod
    def get() -> None:
        pass

    @api.expect(book_model.update())
    @api.marshal_with(fields=None, description="No Content", code=204)
    @staticmethod
    def put() -> None:
        pass

    @api.marshal_with(fields=None, description="No Content", code=204)
    @staticmethod
    def delete() -> None:
        pass