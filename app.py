import os
from flask import Flask, request, render_template, redirect, session, redirect
from lib.database_connection import get_flask_database_connection, DatabaseConnection
from lib.user_repository import *
from lib.login_required import *
from lib.database_connection import DatabaseConnection
from lib.space_repository import SpaceRepository
from lib.space import Space
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.space_repository import SpaceRepository
from lib.user_repository import UserRepository

# Create a new Flask app
app = Flask(__name__)
app.secret_key = 'dev-secret-key'

# == Your Routes Here ==

# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5001/
@app.route('/', methods=['GET'])
def get_index():
    connection = get_flask_database_connection(app)
    spaces_repository = SpaceRepository(connection)
    spaces = spaces_repository.all_with_email()
    return render_template('index.html', spaces=spaces)


@app.route('/login', methods=['GET'])
def get_login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    db_connection = get_flask_database_connection(app)
    user_repo = UserRepository(db_connection)
    login_details = request.form
    user_id = user_repo.verify_user(login_details['email'], login_details['password'])
    if not user_id:
        return redirect('/login')
    session['user_id'] = user_id
    session['email'] = login_details['email']
    return redirect('/')


@app.route('/signup', methods=['GET'])
def get_signup():
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def signup():
    db_connection = get_flask_database_connection(app)
    user_repo = UserRepository(db_connection)
    signup_details = request.form
    if user_repo.check_email_exists(signup_details['email']):
        return redirect('/signup')
    user_repo.create(signup_details['email'], signup_details['password'])
    return redirect('/login')

@app.route('/spaces', methods=["GET"])
@login_required
def get_spaces():
    connection = get_flask_database_connection(app)  
    space_repository = SpaceRepository(connection)        
    return render_template("/spaces.html")

@app.route('/spaces', methods=["POST"])
@login_required
def create_space():
    connection = get_flask_database_connection(app) 
    space_repository = SpaceRepository(connection)
    space_details = request.form
    space = Space(space_details["name"], space_details["address"], space_details["description"], space_details["price_per_night"], session['user_id'])
    space_repository.create(space)
    return redirect("/")




# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

