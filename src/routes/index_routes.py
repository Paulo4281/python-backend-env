from flask import Blueprint

# View Routes
view_routes = Blueprint("view_routes", __name__, url_prefix="/")

# User Routes
user_routes = Blueprint("user_routes", __name__, url_prefix="/user")

# Book Routes
book_routes = Blueprint("book_routes", __name__, url_prefix="/book")
category_routes = Blueprint("category_routes", __name__, url_prefix="/book/category")
author_routes = Blueprint("author_routes", __name__, url_prefix="/book/author")