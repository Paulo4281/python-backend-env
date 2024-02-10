from src.server.server import app
from dotenv import load_dotenv
import os

load_dotenv()

HOST = os.getenv("HOST")
PORT = os.getenv("PORT")
DEBUG = True

if __name__ == "__main__":
    app.run(host=HOST, port=PORT, debug=DEBUG)