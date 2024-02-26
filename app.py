from src.server.server import app
from dotenv import load_dotenv
from os import getenv

load_dotenv()

HOST = getenv("SERVER_HOST")
PORT = getenv("SERVER_PORT")
DEBUG = True

if __name__ == "__main__":
    app.run(host=HOST, port=PORT, debug=DEBUG, threaded=True)