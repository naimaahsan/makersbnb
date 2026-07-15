class Space:
    def __init__(self, name, description, address, price_per_night, user_id=None, id=None):
        self.id = id
        self.name = name
        self.address = address 
        self.description = description 
        self.price_per_night = price_per_night
        self.user_id = user_id

    def __repr__(self):
        return f"Space({self.id}, {self.name}, {self.description}, {self.address}, {self.price_per_night}, {self.user_id})"
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__