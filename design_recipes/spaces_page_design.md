
-- A user is able to see available spaces, including host contact details for booking a space

As a User, in order to see what spaces are available,
I want to see a page showing a list of available spaces
with contact information I can use to book a space.

----------

TESTS

```python
"""
Test that the Index page shows HTML template
for Spaces page (index.html)
"""
def test_spaces_page_shows_available_spaces():
    # connect to the database
    # query db using execute to retrieve spaces details
    # make those results into list of strings
    # assert that list of strings == list that Jinja displays on index page


"""
Test that Index page has sign-up link redirecting to
Sign-up page 
"""
def test_index_page_signup_link():
    # use locator to check sign-up link exists
    # use .click() to make playwright click on sign-up link
    # assert that this redirects to sign-up page

"""
Test that the index page GET request status code is 200
"""
def test_index_page_returns_200():
    # create a test client
    # assert that client.get("/") response is 200

"""
Test that spaces repository can return all spaces
"""
def test_spaces_repository_returns_all_spaces():
    # connect to spaces database
    # instaciate SpacesRepository
    # pass database connection into respository
    # call all() method to get list of strings
    # assert that the list of strings is == seed data

"""
Test spaces model instances with the name, address, discription, ppn, id=None
"""
def test_spaces_model_instances_with_name_address_description_price_per_night_id():
    # Instantiate Spaces model
    # Assert each object attribute == provided variables

"""
Test spaces model formats to strings
"""
def test_spaces_model_formats_to_strings():
    # use given string formatting test

"""
Test two spaces model objects can be easily compared
"""
def test_two_spaces_model_objects_can_be_easily_compared():
    # use given comparison test


```

