import os
from flask import Flask, request, render_template, redirect
from lib.database_connection import get_flask_database_connection
from lib.database_connection import DatabaseConnection
from lib.space_repository import SpaceRepository
from lib.space import Space

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5001/index
@app.route('/index', methods=['GET'])
def get_index():
    return render_template('index.html')

@app.route('/spaces', methods=["GET"])
def get_spaces():
    connection = get_flask_database_connection(app)  
    space_repository = SpaceRepository(connection)        
    spaces = space_repository.all()                     
    return render_template("/spaces.html", spaces=spaces) 

@app.route('/spaces', methods=["POST"])
def create_space():
    connection = get_flask_database_connection(app) 
    space_repository = SpaceRepository(connection)
    space_details = request.form
    space = Space(name= space_details["name"], description = space_details["description"], address = space_details["address"], price_per_night=space_details["price_per_night"])
    space_repository.create(space)
    return redirect("/spaces")


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
