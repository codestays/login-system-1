from flask import Flask, jsonify, request, redirect, session, render_template
from flask_cors import CORS
import json

app = Flask(__name__, template_folder='../client')
CORS(app)


@app.route("/home")
def home():
    return render_template("home.html")

database = {
    "admin":12345,
    "ematshabe023@student.wethinkcode.co.za":"12345"
    }


@app.route("/login-form", methods=["POST", "OPTIONS"])
def login():
    requestData = request.get_data().decode('utf8').replace("'", '"')
    
    if request.method == "POST":
        requestData = json.loads(requestData)
        if requestData["email"] in database: 
            if requestData["password"] == database[requestData["email"]]:
                return jsonify({"message":"you're in", "status":"successful"})
            else:
                return jsonify({"message":"login failed", "status":"error"})
        else:
            return jsonify({"message":"login failed", "status":"error"})

    return jsonify({"response": "done"})
    

@app.route("/registration", methods=["POST"])
def registration():
    formData = request.form
    if request.method == "POST":
        print(formData)
    return "registration page process"


@app.route("/logout", methods=["GET"])
def logout():
    return "logout process"


@app.route("/forgot-password", methods=["POST"])
def forgotPassword():
    return "forgot password process"


if __name__ == '__main__':  
    app.run()  