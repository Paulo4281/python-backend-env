from flask import Flask
from src.routes.user_routes import user_routes
from src.routes.book_routes import book_routes
from src.routes.category_routes import category_routes
from flask_cors import CORS
from flask_restx import Api
from src.database.database_config import *
import os
from dotenv import load_dotenv
from src.docs.modules.book.category_docs import api as category_namespace

load_dotenv()

# App Server & Cors
app = Flask(__name__)
CORS(app, origins="*", send_wildcard=True)

# Routes Blueprint

    # User Routes
app.register_blueprint(user_routes)

    # Book Routes
app.register_blueprint(book_routes)
app.register_blueprint(category_routes)

# End Routes Blueprint

# App Config Credentials
app.config["CORS_HEADERS"] = os.getenv("APP_CORS_HEADERS")
app.config["SECRET_KEY"] = os.getenv("APP_SECRET_KEY")
app.config["RESTX_MASK_SWAGGER"] = False

# API Config
api = Api(
    title="Flask RestFul API",
    version="1.0",
    description="Description",
    doc="/docs"
)

# API Namespaces

    # Book Namespaces
api.add_namespace(category_namespace, path="/book/category")

# API Init
api.init_app(app)