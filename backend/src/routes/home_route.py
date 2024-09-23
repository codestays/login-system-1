from flask import render_template, url_for, request, session, jsonify
import json


def home(app):
    @app.route("/home", methods=["GET"])
    def home():
        return render_template("home.html")