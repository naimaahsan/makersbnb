class Space:
    def __init__(self, name, address, description, price_per_night, id=None):
        self.name = name
        self.address = address
        self.description = description
        self.price_per_night = price_per_night
        self.id = id

    def __repr__(self):
        return f"Space({self.name}, {self.address}, {self.description}, {self.price_per_night:.2f}, {self.id})"
    

