class Booking:
    def __init__(self, space_id, user_id, date, confirmed=False, id=None, space_name=None, price_per_night=None):
        self.id = id
        self.space_id = space_id
        self.user_id = user_id
        self.date = date 
        self.confirmed = confirmed 

# Optional fields from SQL JOIN
        self.space_name = space_name
        self.price_per_night = price_per_night

    def __eq__(self,other):
        return self.__dict__== other.__dict__

    def __repr__(self):
        return f"Booking({self.id}, {self.space_id}, {self.user_id}, '{self.date}', {self.confirmed}, '{self.space_name}', {self.price_per_night})"