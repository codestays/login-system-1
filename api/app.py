from flask import Flask, jsonify, request, redirect, session, render_template
from flask_cors import CORS
import json

app = Flask(__name__, template_folder='../client')
CORS(app)


database = {
    "admin":12345,
    "ematshabe023@student.wethinkcode.co.za":"12345"
}


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
        if requestData["email"] in database: 
            if requestData["password"] == database[requestData["email"]]:
                return jsonify({"message":"you're in", "status":"successful"})
            else:
                return jsonify({"message":"login failed", "status":"error"})
        else:
            return jsonify({"message":"email doesn't exist", "status":"error"})

    return jsonify({"response": "done"})


@app.route("/registration", methods=["GET"])
def registration():
    return render_template("registration-page.html")


@app.route("/registration-form", methods=["POST"])
def registrationForm():
    
    if request.method == "POST":
        requestData = request.get_data().decode('utf8').replace("'", '"') 
        print(requestData)
        # requestData = json.loads(requestData)
        # if requestData["email"] not in database: 
        #     jsonify({"message":"Registration complete", "status":"successful"})
        # else:
        #     return jsonify({"message":"User already exist", "status":"error"})
        return jsonify({"response": "done"})

    return jsonify({"response": "done"})


@app.route("/logout", methods=["GET"])
def logout():
    return "logout process"


@app.route("/forgot-password", methods=["POST"])
def forgotPassword():
    return "forgot password process"


if __name__ == '__main__':  
    app.run()  