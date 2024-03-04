from src.routes.index_routes import view_routes
from flask_cors import cross_origin
from flask_jwt_extended import jwt_required
from flask import render_template

@view_routes.route("/", methods=["GET"])
@cross_origin()
def index() -> str:
    return render_template("/auth/index.html")