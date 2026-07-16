from playwright.sync_api import Page, expect

def login(page: Page):
    page.goto('http://localhost:5001/login')
    page.locator("#email").fill("user1@email.com")
    page.locator("#password").fill("password1")
    page.get_by_role("button", name="Login").click()

def test_booking_page_loads(page: Page, clean_db):
    login(page)
    page.goto('http://localhost:5001/host/bookings')

    h1 = page.locator('h1')
    expect(h1).to_have_text('Bookings requests for my properties')

def test_booking_page_has_expected_bookings(page: Page, clean_db):
    login(page)
    page.goto('http://localhost:5001/host/bookings')
    property_names = page.get_by_test_id('property_name').all_inner_texts()
    assert property_names == [
        'Property: Cool House',
        'Property: Cool House',
        'Property: My House',
        'Property: Cool House',
        'Property: My House'
    ]

def test_booking_page_confirm_button_changes_status(page: Page, clean_db):
    login(page)
    page.goto('http://localhost:5001/host/bookings')
    page.get_by_test_id('button_1').click()
    confirm_statuses = page.get_by_test_id('confirm_status').all_inner_texts()
    assert confirm_statuses == [
        'Confirmed',
        'Pending confirmation',
        'Pending confirmation',
        'Confirmed',
        'Confirmed'
    ]
    page.get_by_test_id('button_2').click()
    confirm_statuses = page.get_by_test_id('confirm_status').all_inner_texts()
    assert confirm_statuses == [
        'Confirmed',
        'Confirmed',
        'Pending confirmation',
        'Confirmed',
        'Confirmed'
    ]