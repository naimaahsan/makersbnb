from lib.booking_repository import BookingRepository

"""
Calling get_bookings_by_host_id using a host id
Returns all the boo
"""
def test_get_bookings_by_host_id(clean_db):
    booking_repo = BookingRepository(clean_db)
    bookings = booking_repo.get_bookings_by_host_id(1)
    assert bookings == [
        { 'booking_id': 1, 'booking_confirmed': False,'requester_email': 'user2@email.com', 'space_name': 'Cool House', 'space_description': 'Small flat', 'space_address': '8 Fake Street, Faketown', 'space_price': 100.00 },
        { 'booking_id': 2, 'booking_confirmed': False,'requester_email': 'user3@email.com', 'space_name': 'Cool House', 'space_description': 'Small flat', 'space_address': '8 Fake Street, Faketown', 'space_price': 100.00 },
        { 'booking_id': 5, 'booking_confirmed': False,'requester_email': 'user1@email.com', 'space_name': 'My House', 'space_description': 'Large flat', 'space_address': '9 Fake Street, Faketown', 'space_price': 125.00 },
        { 'booking_id': 6, 'booking_confirmed': True,'requester_email': 'user2@email.com', 'space_name': 'Cool House', 'space_description': 'Small flat', 'space_address': '8 Fake Street, Faketown', 'space_price': 100.00 },
        { 'booking_id': 7, 'booking_confirmed': True,'requester_email': 'user3@email.com', 'space_name': 'My House', 'space_description': 'Large flat', 'space_address': '9 Fake Street, Faketown', 'space_price': 125.00 }
    ]

"""
Confirming a booking
Changes the booking's confirme state to True
"""
def test_confirm_booking(clean_db):
    booking_repo = BookingRepository(clean_db)
    bookings = booking_repo.get_bookings_by_host_id(1)
    assert bookings[1]['booking_confirmed'] == False
    result = booking_repo.confirm_booking(2)
    assert result is None
    bookings = booking_repo.get_bookings_by_host_id(1)
    print(bookings)
    assert bookings[1]['booking_confirmed'] == True
    assert bookings[0]['booking_confirmed'] == False