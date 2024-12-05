import sys
import os

import routes.forgot_password_route
import routes.home_route
import routes.landing_route
import routes.login_route
import routes.otp_route
import routes.registration_route

sys.path.append(os.path.join(os.path.dirname(__file__), 'database'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'configuration'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'auth'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'routes'))


from flask import Flask
from flask_cors import CORS
from authlib.integrations.flask_client import OAuth
from database import init_db
import os
from configuration import config
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

# routes
routes.landing_route.landing(app)
routes.login_route.login(app)
routes.login_route.google_login(app, oauth)
routes.registration_route.registration(app)
routes.forgot_password_route.forgot_password(app)
routes.otp_route.otp(app)
routes.home_route.home(app)


if __name__ == '__main__':  
    init_db()
    app.run(debug=True)  