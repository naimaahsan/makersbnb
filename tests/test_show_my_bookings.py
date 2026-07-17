from playwright.sync_api import Page, expect


def login(page: Page):
    page.goto('http://localhost:5001/login')
    page.locator("#email").fill("user1@email.com")
    page.locator("#password").fill("password1")
    page.get_by_role("button", name="Login").click()

"""
Test a user who hasn't signed in, tries to view their bookings
"""

def test_non_signed_user_tries_view_bookings(page: Page, db_connection):
    db_connection.seed("seeds/makersbnb.sql")

    page.goto("http://localhost:5001/mybookings")
    assert page.url == "http://localhost:5001/login"

"""
Test a signed user who has bookings, tries to view their bookings
"""

def test_signed_in_user_with_bookings(page: Page, db_connection):
    db_connection.seed("seeds/makersbnb.sql")

    login(page)

    page.goto("http://localhost:5001/mybookings")

    expect(page.get_by_text("My House")).to_be_visible()
    expect(page.get_by_text("Price: £125.0 per night")).to_be_visible()
    expect(page.get_by_text("Top House")).to_be_visible()
    expect(page.get_by_text("Price: £99.0 per night")).to_be_visible()
    expect(page.get_by_text("Date: 2026-05-25")).to_have_count(2)
    expect(page.get_by_text("Pending")).to_have_count(2)


