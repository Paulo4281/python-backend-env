from flask import Flask
from src.routes.user_routes import user_routes
from src.routes.book_routes import book_routes
from src.routes.category_routes import category_routes
from src.routes.view_routes import view_routes
from src.routes.review_routes import review_routes
from flask_cors import CORS
from flask_restx import Api
from src.database.database_config import *
from os import getenv
from dotenv import load_dotenv
from src.docs.modules.book.category_docs import api as category_namespace
from src.docs.modules.book.book_docs import api as book_namespace
from src.docs.modules.book.author_docs import api as author_namespace
from src.docs.modules.user.user_docs import api as user_namespace
from src.docs.modules.book.review_docs import api as review_namespace
from flask_jwt_extended import JWTManager

load_dotenv()

# ------------------------------------------------------------------------------------------------------------------
# App Server & Cors ------------------------------------------------------------------------------------------------------------------

app = Flask(__name__, template_folder="../templates", static_folder="../templates/assets")
CORS(app, origins="*", send_wildcard=True)

# ------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------


# ------------------------------------------------------------------------------------------------------------------
# Routes Blueprint ------------------------------------------------------------------------------------------------------------------

    # View Routes
app.register_blueprint(view_routes)

    # User Routes
app.register_blueprint(user_routes)

    # Book Routes
app.register_blueprint(book_routes)
app.register_blueprint(category_routes)
app.register_blueprint(review_routes)

# End Routes Blueprint ------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------


# ------------------------------------------------------------------------------------------------------------------
# App Config Credentials ------------------------------------------------------------------------------------------------------------------

app.config["CORS_HEADERS"] = getenv("APP_CORS_HEADERS")
app.config["SECRET_KEY"] = getenv("APP_SECRET_KEY")
app.config["RESTX_MASK_SWAGGER"] = False
app.config["JWT_SECRET_KEY"] = getenv("TOKEN_SECRET")
print(app.template_folder)

# ------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------

# JWT Manager

JWTManager(app)

# ------------------------------------------------------------------------------------------------------------------
# API Config ------------------------------------------------------------------------------------------------------------------

api = Api(
    title="Flask RESTFul API",
    version="1.0",
    description="Description",
    doc="/docs"
)

# ------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------------------
# API Namespaces ------------------------------------------------------------------------------------------------------------------

    # User Namespaces
api.add_namespace(user_namespace, path="/user")

    # Book Namespaces
api.add_namespace(book_namespace, path="/book")
api.add_namespace(category_namespace, path="/book/category")
api.add_namespace(author_namespace, path="/book/author")
api.add_namespace(review_namespace, path="/book/review")

# ------------------------------------------------------------------------------------------------------------------
# API Init ------------------------------------------------------------------------------------------------------------------

api.init_app(app)

# ------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------