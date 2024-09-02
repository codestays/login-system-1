from flask import Flask, jsonify, request, redirect, session, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "hello world"

database = {
    "admin":12345,
    "ematshabe023@student.wethinkcode.co.za":12345
    }

@app.route("/login", methods=["POST"])
def login():
    formData = request.form
    
    if request.method == "POST":
        if formData["email"] in database:
            print("avail")
        else:
            print("invalid password")
        
    return "login page process"


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