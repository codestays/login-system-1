import sys
import os

import routes.landing_route
import routes.login_route

sys.path.append(os.path.join(os.path.dirname(__file__), 'database'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'configuration'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'auth'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'routes'))

from flask import Flask, jsonify, request, url_for, session, render_template, redirect
from flask_cors import CORS
from authlib.integrations.flask_client import OAuth
from database import init_db
import json
import os
from configuration import config
import sqlite3
from auth.google_auth.google import google_sign_in
import routes

# set up flask api application
app = Flask(__name__, template_folder="../../frontend", static_folder="../../frontend/static")
app.secret_key = os.urandom(20)
CORS(app)
oauth = OAuth(app)
oauth.init_app(app)

# connect to google
google = google_sign_in(oauth, config.client_id, config.client_secret)


routes.landing_route.landing(app)
routes.login_route.login(app)
routes.login_route.google_login(app, oauth)

if __name__ == '__main__':  
    init_db()
    app.run(debug=True)  