
def google_sign_in(oauth, client_id, client_secret):
    google = oauth.register(
        name='login1',
        client_id=client_id,
        client_secret=client_secret,
        access_token_url='https://oauth2.googleapis.com/token',
        authorize_url='https://accounts.google.com/o/oauth2/auth',
        server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
        authorize_params=None,
        access_token_params=None,
        refresh_token_url=None,
        redirect_uri='http://localhost:5000/login-google-form',
        client_kwargs={'scope': 'openid profile email'},
    )
    return google