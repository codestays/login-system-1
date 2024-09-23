from flask import request, render_template, jsonify
import json
import random


def generate_random_numbers():
    numbers = [str(random.randint(0, 9)) for _ in range(4)] 
    return ''.join(numbers) 


def registration(app):
    @app.route("/registration", methods=["GET"])
    def registration():
        return render_template("registration.html")


    @app.route("/registration-form", methods=["POST"])
    def registrationForm():
        code = generate_random_numbers()
        print(code)
        
        if request.method == "POST":
            requestData = request.json

            email = requestData["email"]
            name = requestData["name"]
            surname = requestData["surname"]
            password = requestData["password"]

            return jsonify({"code":code, "status": "200"})        

        return jsonify({"message":"none", "status":"error"})