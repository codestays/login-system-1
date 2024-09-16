from flask import Flask, jsonify, request, redirect, session, render_template
from flask_cors import CORS
import json

app = Flask(__name__, template_folder='../client')
CORS(app)


db = {}

@app.route("/")
def root():
    return render_template("login-page.html")


@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/login")
def login():
    return render_template("login-page.html")


@app.route("/login-form", methods=["POST"])
def loginForm():
    requestData = request.get_data().decode('utf8').replace("'", '"')
    
    if request.method == "POST":
        requestData = json.loads(requestData)
        if requestData["email"] in db: 
            if requestData["password"] == db[requestData["email"]]["password"]:
                return jsonify({"message":"you're in", "status":"successful"})
            else:
                return jsonify({"message":"login failed", "status":"error"})
        else:
            return jsonify({"message":"email doesn't exist", "status":"error"})

    return jsonify({"message":"none", "status":"error"})


@app.route("/registration", methods=["GET"])
def registration():
    return render_template("registration-page.html")


@app.route("/registration-form", methods=["POST"])
def registrationForm():
    if request.method == "POST":
        requestData = request.get_data().decode('utf8').replace("'", '"') 
        requestData = json.loads(requestData)

        if requestData["email"] not in db:
            db[requestData["email"]] = requestData
            return jsonify({"message":"registration complete", "status":"successful"})
        else:
            return jsonify({"message":"user already exist", "status":"error"})        

    return jsonify({"message":"none", "status":"error"})


@app.route("/logout", methods=["GET"])
def logout():
    return "logout process"


@app.route("/forgot-password", methods=["POST"])
def forgotPassword():
    return "forgot password process"


if __name__ == '__main__':  
    app.run()  