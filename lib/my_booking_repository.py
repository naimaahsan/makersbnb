from lib.my_booking import MyBooking

class MyBookingRepository:
    def __init__(self, connection):
        self._connection = connection 

    def find_by_user_id(self, user_id):
        rows = self._connection.execute('SELECT bookings.id, bookings.space_id, ' \
        'bookings.user_id, bookings.date, bookings.confirmed, spaces.name AS space_name,' \
        'spaces.address AS spaces_address, spaces.price_per_night FROM bookings JOIN spaces ON bookings.space_id = spaces.id WHERE bookings.user_id = %s ORDER BY bookings.date ASC', [user_id])

        bookings = []
        for row in rows:
            item = MyBooking(row["space_id"], row["user_id"], row["date"], id=row["id"], 
                            confirmed=row["confirmed"], space_name=row["space_name"], 
                            space_address=row["spaces_address"], price_per_night=float(row["price_per_night"]))
            
            bookings.append(item)
        return bookings