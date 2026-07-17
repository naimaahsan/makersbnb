from playwright.sync_api import Page, expect

def test_user_create_new_space_journey(page: Page, clean_db):

    page.goto('http://localhost:5001/')
    h1 = page.locator('h1')
    expect(h1).to_have_text('Explore Spaces')
    page.get_by_text("Sign Up").click()

    sign_up_h1 = page.locator('h1')
    expect(sign_up_h1).to_have_text('Sign-Up')
    page.locator("#email").fill("random@gmail.com")
    page.locator("#password").fill("random")
    page.get_by_role("button", name="Sign-up").click()
    expect(page).to_have_url("http://localhost:5001/login")

    log_in_h1 = page.locator('h1')
    expect(log_in_h1).to_have_text('Log In')
    page.locator("#email").fill("random@gmail.com")
    page.locator("#password").fill("random")
    page.get_by_role("button", name="Login").click()
    expect(page).to_have_url("http://localhost:5001/")

    page.get_by_text("List your Space").click()
    create_space_h1 = page.locator('h1')
    expect(create_space_h1).to_have_text('List your Space')
    page.get_by_placeholder("Name *").fill('ASDASDASDASDASD')
    page.get_by_placeholder("Description *").fill('ASDASDASDASDASD1')
    page.get_by_placeholder("Address *").fill('1 fakeplace, fakertown')
    page.get_by_placeholder("Price per night *").fill('90.00')
    page.get_by_role("button", name="Submit").click()
    expect(page).to_have_url("http://localhost:5001/")


