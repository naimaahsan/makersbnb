from lib.booking import Booking

class BookingRepository:
    def __init__(self, connection):
        self._connection = connection

    def get_bookings_by_host_id(self, host_id):
        """
        Returns:
        A list of dictionaries containing
        1) Email of the person requesting the booking
        2) Details of the space
        3) Date of the booking request
        4) Confirmed status of booking request
        """
        return self._connection.execute(
            "SELECT bookings.id AS booking_id, bookings.confirmed AS booking_confirmed, users.email AS requester_email, " \
            "spaces.name as space_name, spaces.description AS space_description, spaces.address AS space_address, " \
            "spaces.price_per_night AS space_price " \
            "FROM bookings " \
            "JOIN users " \
            "ON bookings.user_id = users.id " \
            "JOIN spaces " \
            "ON bookings.space_id = spaces.id " \
            "WHERE spaces.user_id = %s " \
            "ORDER BY bookings.id ASC;", [host_id]
        )
    
    def confirm_booking(self, booking_id):
        self._connection.execute(
            "UPDATE bookings " \
            "SET confirmed = TRUE " \
            "WHERE id = %s", [booking_id]
        )
        return None
    
    def create_booking(self, booking):
        self._connection.execute("INSERT INTO bookings (space_id, user_id, date, confirmed) VALUES (%s, %s, %s, %s)", [booking.space_id, booking.user_id, booking.date, booking.confirmed])
        return None