from flask import render_template

def landing(app):
    @app.route("/")
    def root():
        return render_template("landing.html")