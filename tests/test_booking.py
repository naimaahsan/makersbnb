from lib.booking import Booking
import datetime

def test_create_booking():
    booking = Booking(1, 1, datetime.date(2000, 1, 1), False, 2)

    assert booking.id == 2
    assert booking.space_id == 1
    assert booking.user_id == 1
    assert booking.date == datetime.date(2000, 1, 1)
    assert booking.confirmed == False

def test_booking_equality():
    booking1 = Booking(1, 1, datetime.date(2000, 1, 1), False, 3)
    booking2 = Booking(1, 1, datetime.date(2000, 1, 1), False, 3)
    
    assert booking1 == booking2

def test_booking_str():
    booking = Booking(1, 1, datetime.date(2000, 1, 1), False, 4)

    assert str(booking) == "Booking(4, 1, 1, 2000-01-01, False)"