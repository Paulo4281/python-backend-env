from flask_restx import Namespace, Resource
from src.modules.book.models.author_model import AuthorModel
from src.utils.app_docs_auth import authorizations

api = Namespace("Author", authorizations=authorizations)
author_model = AuthorModel(api)

@api.doc(security="jsonwebtoken")
@api.route("/")
class AuthorResource(Resource):
    @api.expect(author_model.save())
    @api.marshal_with(fields=author_model.find(), description="Created", code=201)
    @staticmethod
    def post() -> None:
        pass

    @api.marshal_with(fields=author_model.find(), as_list=True)
    @staticmethod
    def get() -> None:
        pass

@api.doc(security="jsonwebtoken")
@api.route("/<id_>")
class AuthorResourceDetail(Resource):
    @api.marshal_with(fields=author_model.find_by_id())
    @staticmethod
    def get() -> None:
        pass