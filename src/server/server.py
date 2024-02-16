from flask import Flask
from src.routes.user_routes import user_routes
from src.routes.book_routes import book_routes
from flask_cors import CORS
from src.database.database_config import *
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app, origins="*", send_wildcard=True)

app.config["CORS_HEADERS"] = os.getenv("APP_CORS_HEADERS")
app.config["SECRET_KEY"] = os.getenv("APP_SECRET_KEY")

app.register_blueprint(user_routes)
app.register_blueprint(book_routes)