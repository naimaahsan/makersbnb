class MyBooking:
    def __init__(self, space_id, user_id, date, confirmed=False, id=None, space_name=None, space_address=None, price_per_night=None):
        self.id = id
        self.space_id = space_id
        self.user_id = user_id
        self.date = date 
        self.confirmed = confirmed 

        self.space_address = space_address
        self.space_name = space_name
        self.price_per_night = price_per_night

    def __eq__(self,other):
        return self.__dict__== other.__dict__

    def __repr__(self):
        return f"MyBooking({self.id}, {self.space_id}, {self.user_id}, '{self.date}', {self.confirmed}, '{self.space_name}', '{self.space_address}', {self.price_per_night})"