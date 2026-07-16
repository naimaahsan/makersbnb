import datetime 
from lib.booking import *


def test_instantiates():
    test_date = datetime.date(2026,1,1)
    booking = Booking(1,2, test_date, confirmed = True, id=1, space_name= "Cool House", price_per_night= 100.00)
    assert booking.space_id == 1
    assert booking.user_id == 2
    assert booking.date == test_date
    assert booking.space_name == "Cool House"
    assert booking.confirmed is True
    assert booking.price_per_night == 100.00 
    assert booking.id == 1

def test_equality():
    test_date = datetime.date(2026, 1, 1)
    booking = Booking(1,2,test_date, True, 1)
    booking_2 = Booking(1,2,test_date, True, 1)
    assert booking == booking_2

def test_formats_correctly():
    test_date = datetime.date(2026, 1, 1)
    booking = Booking(1,2, test_date, confirmed = True, id=1, space_name= "Cool House", price_per_night= 100.00)
    assert repr(booking) == "Booking(1, 1, 2, '2026-01-01', True, 'Cool House', 100.0)"