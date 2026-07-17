from lib.booking import Booking, HostBooking

class BookingRepository:
    def __init__(self, connection):
        self._connection = connection        

    def get_bookings_by_host_id(self, host_id):
        rows = self._connection.execute(
            "SELECT bookings.id AS booking_id, bookings.confirmed AS booking_confirmed, users.email AS requester_email, " \
            "spaces.name AS space_name, users.id AS user_id, bookings.date AS booking_date, " \
            "bookings.space_id AS space_id " \
            "FROM bookings " \
            "JOIN users " \
            "ON bookings.user_id = users.id " \
            "JOIN spaces " \
            "ON bookings.space_id = spaces.id " \
            "WHERE spaces.user_id = %s " \
            "ORDER BY bookings.id ASC;", [host_id]
        )
        return [HostBooking(row['space_id'], row['user_id'], row['booking_date'],
                            row['booking_confirmed'], row['requester_email'], row['space_name'],
                            row['booking_id']) for row in rows]
    
    def confirm_booking(self, booking_id):
        self._connection.execute(
            "UPDATE bookings " \
            "SET confirmed = TRUE " \
            "WHERE id = %s", [booking_id]
        )
        return None
    
    def find_host_id_by_booking_id(self, id):
        host_ids = self._connection.execute(
            "SELECT users.id AS id FROM bookings " \
            "JOIN spaces " \
            "ON bookings.space_id = spaces.id " \
            "JOIN users " \
            "ON spaces.user_id = users.id " \
            "WHERE bookings.id = %s;", [id],
        )
        if len(host_ids) != 1:
            return None
        return host_ids[0]['id']
    
    def create_booking(self, booking):
        self._connection.execute("INSERT INTO bookings (space_id, user_id, date, confirmed) VALUES (%s, %s, %s, %s)", [booking.space_id, booking.user_id, booking.date, booking.confirmed])
        return None
    
    def valid_booking(self, booking):

        already_booked = []

        rows = self._connection.execute("SELECT * FROM bookings WHERE space_id = %s AND date = %s AND confirmed = True", [booking.space_id, booking.date])

        for row in rows:
            already_booked.append(row)

        if already_booked:
            return False
        else:
            return True
        
    def delete_booking(self, id):
        self._connection.execute(
            "DELETE FROM bookings " \
            "WHERE id = %s", [id]
        )

    def check_confirmed(self, id):
        rows = self._connection.execute(
            "SELECT * FROM bookings " \
            "WHERE id = %s", [id]
        )
        if not rows:
            return False
        return rows[0]['confirmed']
