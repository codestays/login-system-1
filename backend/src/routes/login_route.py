from flask import render_template, url_for

def login(app):
    @app.route("/login")
    def login():
        return render_template("login.html")


def google_login(app, oauth):
    @app.route("/login-google")
    def gAuth():
        return oauth.login1.authorize_redirect(redirect_uri=url_for('googlel_form', _external=True))
    

    @app.route("/login-google-form")
    def googlel_form():
        
        return "store data from google"