from flask import render_template, url_for, request, session, jsonify
import json


def otp(app):
    @app.route("/otp-form", methods=["POST"])
    def opt():
        if request.method == "POST":
            requestData = request.json
            print(requestData)

            return jsonify({"status":"200"})
        return jsonify({"status":"100"})