from src.server.server import app
from dotenv import load_dotenv
import os

load_dotenv()

HOST = os.getenv("SERVER_HOST")
PORT = os.getenv("SERVER_PORT")
DEBUG = True

if __name__ == "__main__":
    app.run(host=HOST, port=PORT, debug=DEBUG)