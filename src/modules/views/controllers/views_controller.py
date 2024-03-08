from flask import render_template, request, jsonify, Response
from jwt import decode
from os import getenv

class ViewController:

    @staticmethod
    def verify() -> Response:
        if request.json["headers"]["authorization"]:
            token = request.json["headers"]["authorization"].split(" ")[1]
            try:
                decode(token, getenv("TOKEN_SECRET"), algorithms="HS256")
            except Exception as e:
                print(str(e))
                return jsonify({"status": "Not authorized."})
        return jsonify({"status": "authorized"})

    @staticmethod
    def index() -> str:
        return render_template("/login/index.html")

    @staticmethod
    def dash() -> str:
        return render_template("/dash/index.html")