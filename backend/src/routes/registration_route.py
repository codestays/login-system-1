from flask import request, render_template, jsonify
import json

def registration(app):
    @app.route("/registration", methods=["GET"])
    def registration():
        return render_template("registration.html")


    @app.route("/registration-form", methods=["POST"])
    def registrationForm():
        code = "1234"
        
        if request.method == "POST":
            requestData = request.json

            email = requestData["email"]
            name = requestData["name"]
            surname = requestData["surname"]
            password = requestData["password"]

            return jsonify({"code":code, "status": "200"})        

        return jsonify({"message":"none", "status":"error"})