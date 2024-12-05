from flask import render_template, url_for, request, session, jsonify
import json
import sqlite3

def login(app):
    @app.route("/login")
    def login():
        return render_template("login.html")
    

    @app.route("/login-form", methods=["POST"])
    def loginForm():
        
        if request.method == "POST":
            requestData = request.json
            print(requestData)

            return jsonify({"status":"200"})

        return jsonify({"message": "none", "status": "error"})


def google_login(app, oauth):
    @app.route("/login-google")
    def gAuth():
        return oauth.login1.authorize_redirect(redirect_uri=url_for('googlel_form', _external=True))
    

    @app.route("/login-google-form", methods=["GET"])
    def googlel_form():
        
        return "store data from google"