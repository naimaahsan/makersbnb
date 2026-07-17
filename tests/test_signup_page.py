from playwright.sync_api import Page, expect

"""
Test that the signup page loads and has the required title
"""
def test_login_page_elements(page: Page):
    page.goto('http://localhost:5001/signup')

    h1 = page.locator('h1')
    expect(h1).to_have_text('Sign-Up')

"""
Test that a user with a new email and valid password can sign-up
"""
def test_login_page_with_valid_login_details(page: Page, clean_db):
    page.goto('http://localhost:5001/signup')

    h1 = page.locator('h1')
    expect(h1).to_have_text('Sign-Up')
    page.locator("#email").fill("newemail@email.com")
    page.locator("#password").fill("password1")
    page.get_by_role("button", name="Sign-up").click()
    expect(page).to_have_url("http://localhost:5001/login")

"""
Test that the a user with a non-unique email can't sign-up
"""
def test_login_page_with_valid_login_details(page: Page, clean_db):
    page.goto('http://localhost:5001/signup')

    h1 = page.locator('h1')
    expect(h1).to_have_text('Sign-Up')
    page.locator("#email").fill("user1@email.com")
    page.locator("#password").fill("password1234")
    page.get_by_role("button", name="Sign-up").click()
    expect(page).to_have_url("http://localhost:5001/signup")