from playwright.sync_api import Page, expect

"""
Test that the login page loads has the required title
"""
def test_login_page_elements(page: Page, clean_db):
    page.goto('http://localhost:5001/login')

    h1 = page.locator('h1')
    expect(h1).to_have_text('Log In')

"""
Test that the a user with valid credentials can log in
"""
def test_login_page_with_valid_login_details(page: Page, clean_db):
    page.goto('http://localhost:5001/login')

    h1 = page.locator('h1')
    expect(h1).to_have_text('Log In')
    page.locator("#email").fill("user1@email.com")
    page.locator("#password").fill("password1")
    page.get_by_role("button", name="Login").click()
    expect(page).to_have_url("http://localhost:5001/")

"""
Test that the a user with invalid credentials is not logged in
"""
def test_login_page_with_invalid_login_details_fails(page: Page, clean_db):
    page.goto('http://localhost:5001/login')

    h1 = page.locator('h1')
    expect(h1).to_have_text('Log In')
    page.locator("#email").fill("user1@email.com")
    page.locator("#password").fill("password12")
    page.get_by_role("button", name="Login").click()
    expect(page).to_have_url("http://localhost:5001/login")