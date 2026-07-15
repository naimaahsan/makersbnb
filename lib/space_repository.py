from lib.space import Space

class SpaceRepository:
    def __init__(self, db_conn):
        self._connection = db_conn

    def all(self):
        rows = self._connection.execute("SELECT * FROM spaces;")

        spaces = []
        for row in rows:

            item = Space(row["name"], row["description"], row["address"], row["price_per_night"], row["user_id"], row["id"])
            spaces.append(item)

        return spaces
        
    def create(self, space):
        self._connection.execute(
            'INSERT INTO spaces (name, description, address, price_per_night, user_id) VALUES (%s, %s, %s, %s, %s)', 
            [space.name, space.description, space.address, space.price_per_night, space.user_id])
        
        return None