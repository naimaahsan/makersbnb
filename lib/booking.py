class Booking:
    def __init__(self, space_id, user_id, date, confirmed, id=None):
        self.id = id
        self.space_id = space_id
        self.user_id = user_id
        self.date = date
        self.confirmed = confirmed

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Booking({self.id}, {self.space_id}, {self.user_id}, {self.date}, {self.confirmed})"
    

class HostBooking:
    def __init__(self, space_id, user_id, date, confirmed, requester_email, space_name, id=None):
        self.id = id
        self.space_id = space_id
        self.user_id = user_id
        self.date = date
        self.confirmed = confirmed
        self.requester_email = requester_email
        self.space_name = space_name

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"HostBooking({self.id}, {self.space_id}, {self.user_id}, {self.date}, {self.confirmed}, {self.requester_email}, {self.space_name})"