# Login system
This project is a user login system built using Flask for the backend API, HTML for the front-end, SQLite as the database, and JavaScript for handling user interactions on the client-side.

## Features
* User Registration: Allows users to register with their name, surname, email, and password.
* User Login: Authenticates users using their email and password.
* Google OAuth Login: Users can log in via their Google account using OAuth 2.0.
* Session Management: Keeps users logged in across different pages.
* Logout: Users can securely log out, clearing their session.


## Technology Stack
* Backend: Flask (Python)
* Frontend: HTML, CSS, JavaScript
* Database: SQLite
* OAuth: Google OAuth 2.0 (Authlib)
* Cross-Origin Resource Sharing: Flask-CORS for handling CORS issues


## Installation
1. Clone the repository
````bash
git clone https://github.com/codestays/login-system-1.git
cd login-system-1
````

2. Install dependencies
Make sure you have Python 3 and pip installed. Install the required dependencies:
````bash
pip install -r requirements.txt
````

3. Run the Application
Once everything is set up, run the Flask application:
````bash
cd app
python app.py
````
