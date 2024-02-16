from flask import Blueprint

user_routes = Blueprint("user_routes", __name__, url_prefix="/user")
book_routes = Blueprint("book_routes", __name__, url_prefix="/book")