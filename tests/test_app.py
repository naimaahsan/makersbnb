from playwright.sync_api import Page, expect
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app


# Tests for your routes go here

"""
Test index page GET request returns 200 response
"""
def test_index_page_returns_200():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200


"""
We can render the index page and show spaces
"""
# def test_get_index(page, test_web_address):
#     # We load a virtual browser and navigate to the / page
#     page.goto(f"http://{test_web_address}/")

#     # We look at the <p> tag
#     p_tag = page.locator("p")

#     # We assert that it has the text "This is the homepage."
#     #expect(p_tag).to_have_text("This is the homepage.")