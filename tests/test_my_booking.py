import datetime 
from lib.my_booking import *


def test_instantiates():
    test_date = datetime.date(2026,1,1)
    booking = MyBooking(1,2, test_date, confirmed = True, id=1, space_name= "Cool House", space_address= "8 Fake Street, Faketown", price_per_night= 100.00)
    assert booking.space_id == 1
    assert booking.user_id == 2
    assert booking.date == test_date
    assert booking.space_name == "Cool House"
    assert booking.confirmed is True
    assert booking.price_per_night == 100.00 
    assert booking.id == 1
    assert booking.space_address == "8 Fake Street, Faketown"

def test_equality():
    test_date = datetime.date(2026, 1, 1)
    booking = MyBooking(1,2,test_date, True, 1)
    booking_2 = MyBooking(1,2,test_date, True, 1)
    assert booking == booking_2

def test_formats_correctly():
    test_date = datetime.date(2026, 1, 1)
    booking = MyBooking(1,2, test_date, confirmed = True, id=1, space_name= "Cool House", space_address= "8 Fake Street, Faketown", price_per_night= 100.00)
    assert repr(booking) == "MyBooking(1, 1, 2, '2026-01-01', True, 'Cool House', '8 Fake Street, Faketown', 100.0)"