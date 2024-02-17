from flask import Blueprint

#User Routes
user_routes = Blueprint("user_routes", __name__, url_prefix="/user")

# Book Routes
book_routes = Blueprint("book_routes", __name__, url_prefix="/book")
category_routes = Blueprint("category_routes", __name__, url_prefix="/book/category")