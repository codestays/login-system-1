from flask import render_template, url_for, request, session, jsonify
import json


def forgot_password(app):
    @app.route("/forgot-password", methods=["GET"])
    def forgot_pass():
        return render_template("forgot-password.html")
    

    @app.route("/forgot-password-form", methods=["POST"])
    def forgot_form():
        if request.method == "POST":
            requestData = request.json
            print(requestData)

            return jsonify({"status":"200"})
        
        return jsonify({"status":"200"})
        
    