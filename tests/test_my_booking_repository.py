from lib.my_booking_repository import *
from lib.my_booking import *
import datetime

def test_find_bookings_with_user_id(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    my_booking_repository = MyBookingRepository(db_connection)
    bookings = my_booking_repository.find_by_user_id(2)

    assert len(bookings) == 3

    assert bookings == [
        MyBooking(1, 2, datetime.date(2026, 1, 1), id=1, confirmed=False, space_name="Cool House", space_address="8 Fake Street, Faketown", price_per_night=100.00),
        MyBooking(3, 2, datetime.date(2026, 1, 7), id=3, confirmed=False, space_name="Top House", space_address="15 Fake Road, Faketown", price_per_night=99.00),
        MyBooking(1, 2, datetime.date(2026, 2, 2), id=6, confirmed=True, space_name="Cool House", space_address="8 Fake Street, Faketown", price_per_night=100.00)]


