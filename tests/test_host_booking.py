from lib.booking import HostBooking

from lib.booking import Booking
import datetime

def test_create_booking():
    booking = HostBooking(1, 1, datetime.date(2000, 1, 1), False, 'a@email.com', 'Space name', 2)

    assert booking.id == 2
    assert booking.space_id == 1
    assert booking.user_id == 1
    assert booking.date == datetime.date(2000, 1, 1)
    assert booking.confirmed == False
    assert booking.requester_email == 'a@email.com'
    assert booking.space_name == 'Space name'

def test_booking_equality():
    booking1 = HostBooking(1, 1, datetime.date(2001, 1, 1), False, 'a@email.com', 'Space name1', 3)
    booking2 = HostBooking(1, 1, datetime.date(2001, 1, 1), False, 'a@email.com', 'Space name1', 3)
    
    assert booking1 == booking2

def test_booking_str():
    booking = HostBooking(1, 1, datetime.date(2000, 1, 1), False, 'a@email.com', 'Space name', 4)

    assert str(booking) == "HostBooking(4, 1, 1, 2000-01-01, False, a@email.com, Space name)"