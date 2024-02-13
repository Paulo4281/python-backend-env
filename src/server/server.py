from flask import Flask
from src.routes.user_routes import user_routes
from src.database.database_config import *

app = Flask(__name__)

app.register_blueprint(user_routes)