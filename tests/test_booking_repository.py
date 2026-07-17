from lib.booking_repository import BookingRepository
from lib.booking import Booking, HostBooking
import datetime

"""
Calling get_bookings_by_host_id using a host id
Returns all the boo
"""
def test_get_bookings_by_host_id(clean_db):
    booking_repo = BookingRepository(clean_db)
    bookings = booking_repo.get_bookings_by_host_id(1)
    assert bookings == [
        HostBooking(1, 2, datetime.date(2026, 1, 1), False, 'user2@email.com', 'Cool House', 1), 
        HostBooking(1, 3, datetime.date(2026, 1, 3), False, 'user3@email.com', 'Cool House', 2), 
        HostBooking(2, 1, datetime.date(2026, 5, 25), False, 'user1@email.com', 'My House', 5),
        HostBooking(1, 2, datetime.date(2026, 2, 2), True, 'user2@email.com', 'Cool House', 6),
        HostBooking(2, 3, datetime.date(2026, 3, 5), True, 'user3@email.com', 'My House', 7) 
    ]

"""
Confirming a booking
Changes the booking's confirme state to True
"""
def test_confirm_booking(clean_db):
    booking_repo = BookingRepository(clean_db)
    bookings = booking_repo.get_bookings_by_host_id(1)
    assert bookings[1].confirmed == False
    result = booking_repo.confirm_booking(2)
    assert result is None
    bookings = booking_repo.get_bookings_by_host_id(1)
    print(bookings)
    assert bookings[1].confirmed == True
    assert bookings[0].confirmed == False

"""
Calling find booking
Returns the booking with that id
"""
def test_find_booking_with_host_id(clean_db):
    booking_repo = BookingRepository(clean_db)
    host_id = booking_repo.find_host_id_by_booking_id(1)
    assert host_id == 1
    host_id = booking_repo.find_host_id_by_booking_id(3)
    assert host_id == 2

"""
Creating a booking inserts new booking data 
"""
def test_create_booking(clean_db, db_connection):
    booking_repo = BookingRepository(clean_db)

    test_booking = Booking(1, 3, "2000-01-01")

    booking_repo.create_booking(test_booking)

    row = db_connection.execute("SELECT * FROM bookings WHERE id = 8;")[0]

    latest_booking = Booking(row["space_id"], row["user_id"], row["date"], row["confirmed"], row["id"])

    print(latest_booking.date)

    assert latest_booking.id == 8
    assert latest_booking.space_id == 1
    assert latest_booking.user_id == 3
    assert latest_booking.date == datetime.date(2000, 1, 1)
    assert latest_booking.confirmed == False

def test_delete_booking(clean_db):
    booking_repo = BookingRepository(clean_db)
    bookings = booking_repo.get_bookings_by_host_id(1)
    assert len(bookings) == 5

    result = booking_repo.delete_booking(5)
    assert result is None
    bookings = booking_repo.get_bookings_by_host_id(1)
    assert len(bookings) == 4
    assert HostBooking(2, 1, datetime.date(2026, 5, 25), False, 'user1@email.com', 'My House', 5) not in bookings
    assert bookings == [
        HostBooking(1, 2, datetime.date(2026, 1, 1), False, 'user2@email.com', 'Cool House', 1), 
        HostBooking(1, 3, datetime.date(2026, 1, 3), False, 'user3@email.com', 'Cool House', 2), 
        HostBooking(1, 2, datetime.date(2026, 2, 2), True, 'user2@email.com', 'Cool House', 6),
        HostBooking(2, 3, datetime.date(2026, 3, 5), True, 'user3@email.com', 'My House', 7) 
    ]

def test_check_booking_confirmed(clean_db):
    booking_repo = BookingRepository(clean_db)
    confirmed1 = booking_repo.check_confirmed(7)
    assert confirmed1 == True
    confirmed2 = booking_repo.check_confirmed(1)
    assert confirmed2 == False