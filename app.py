import os
from flask import Flask, request, render_template, redirect, session
from lib.database_connection import get_flask_database_connection, DatabaseConnection
from lib.user_repository import *

# Create a new Flask app
app = Flask(__name__)
app.secret_key = 'dev-secret-key'
db_connection = DatabaseConnection()
db_connection.connect()
user_repo = UserRepository(db_connection)

# == Your Routes Here ==

# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5001/index
@app.route('/index', methods=['GET'])
def get_index():
    return render_template('index.html')

@app.route('/login', methods=['GET'])
def get_login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    login_details = request.form
    user_id = user_repo.verify_user(login_details['email'], login_details['password'])
    if not user_id:
        return redirect('/login')
    session['user_id'] = user_id
    session['email'] = login_details['email']
    return redirect('/index')


@app.route('/signup', methods=['GET'])
def get_signup():
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def signup():
    signup_details = request.form
    if user_repo.check_email_exists(signup_details['email']):
        return redirect('/signup')
    user_repo.create(signup_details['email'], signup_details['password'])
    return redirect('/login')

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
    db_connection.seed('seeds/makersbnb.sql')
