from flask import Flask, jsonify, request, url_for, session, render_template, redirect
from flask_cors import CORS
from authlib.integrations.flask_client import OAuth
from database import init_db
import json
import os
import config
import sqlite3


app = Flask(__name__, template_folder='../client')
CORS(app)

app.secret_key = os.urandom(20)
oauth = OAuth(app)
oauth.init_app(app)
google = oauth.register(
    name='login1',
    client_id=config.client_id,
    client_secret=config.client_secret,
    access_token_url='https://oauth2.googleapis.com/token',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
    authorize_params=None,
    access_token_params=None,
    refresh_token_url=None,
    redirect_uri='http://localhost:5000/login-google-form',
    client_kwargs={'scope': 'openid profile email'},
)


db = {}


@app.route("/")
def root():
    return render_template("login-page.html")


@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/login-google")
def gAuth():
    return oauth.login1.authorize_redirect(redirect_uri=url_for('gAuthForm', _external=True))


@app.route("/login-google-form")
def gAuthForm():
    token = google.authorize_access_token()
    session['name'] = token
    email = token["userinfo"]["email"]
    name = token["userinfo"]["given_name"]
    surname = token["userinfo"]["family_name"]
    password = token["access_token"]

    conn = sqlite3.connect('login.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
    existing_user = cursor.fetchone()
    
    if not existing_user:
        cursor.execute("INSERT INTO users (name, surname, email, password) VALUES (?, ?, ?, ?)",
                    (name, surname, email, password))
        conn.commit()
        conn.close()
    
    session["name"] = email

    return redirect(url_for('home'))


@app.route("/login")
def login():
    return render_template("login-page.html")


@app.route("/login-form", methods=["POST"])
def loginForm():
    requestData = request.get_data().decode('utf8').replace("'", '"')
    
    if request.method == "POST":
        requestData = json.loads(requestData)
        email = requestData["email"]
        password = requestData["password"]

        conn = sqlite3.connect('login.db')
        cursor = conn.cursor()

        cursor.execute("SELECT password FROM users WHERE email = ?", (email,))
        user = cursor.fetchone()

        if user:
            if password == user[0]:
                session["name"] = email
                return jsonify({"message": "you're in", "status": "successful"})
            else:
                return jsonify({"message": "login failed", "status": "error"})
        else:
            return jsonify({"message": "email doesn't exist", "status": "error"})

    return jsonify({"message": "none", "status": "error"})


@app.route("/registration", methods=["GET"])
def registration():
    return render_template("registration-page.html")


@app.route("/registration-form", methods=["POST"])
def registrationForm():
    if request.method == "POST":
        requestData = request.get_data().decode('utf8').replace("'", '"') 
        requestData = json.loads(requestData)

        email = requestData["email"]
        name = requestData["name"]
        surname = requestData["surname"]
        password = requestData["password"]
        
        conn = sqlite3.connect('login.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        existing_user = cursor.fetchone()

        if existing_user:
            return jsonify({"message": "user already exists", "status": "error"})
        else:
            # Insert new user
            cursor.execute("INSERT INTO users (name, surname, email, password) VALUES (?, ?, ?, ?)",
                      (name, surname, email, password))
            conn.commit()
            conn.close()
            return jsonify({"message": "registration complete", "status": "successful"})        

    return jsonify({"message":"none", "status":"error"})


@app.route("/logout", methods=["GET"])
def logout():
    return redirect(url_for("/"))


@app.route("/forgot-password", methods=["POST"])
def forgotPassword():
    return "forgot password process"


if __name__ == '__main__':  
    init_db()
    app.run()  