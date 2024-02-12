from flask import Flask
from src.routes.user_session_routes import user_session_routes

app = Flask(__name__)

app.register_blueprint(user_session_routes)