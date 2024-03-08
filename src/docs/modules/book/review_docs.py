from flask_restx import Namespace, Resource
from src.modules.book.models.review_model import ReviewModel
from src.utils.app_docs_auth import authorizations

api = Namespace("Review", authorizations=authorizations)
review_model = ReviewModel(api)

@api.doc(security="jsonwebtoken")
@api.route("/")
class ReviewResource(Resource):
    @api.expect(review_model.save())
    @api.marshal_with(fields=review_model.find(), description="Created", code=201)
    @staticmethod
    def post() -> None:
        pass

    @api.marshal_with(fields=review_model.find(), as_list=True)
    @staticmethod
    def get() -> None:
        pass

@api.doc(security="jsonwebtoken")
@api.route("/<id_>")
class ReviewResourceDetail(Resource):
    @api.marshal_with(fields=review_model.find_by_id())
    @staticmethod
    def get() -> None:
        pass

    @api.marshal_with(fields=None, description="No Content", code=204)
    @staticmethod
    def delete() -> None:
        pass