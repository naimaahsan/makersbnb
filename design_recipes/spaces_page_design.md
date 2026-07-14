
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
Test that 
"""



```

