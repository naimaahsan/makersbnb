from lib.space import Space

class SpaceRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT name, address, description, price_per_night, id FROM spaces')
        spaces = []
        for row in rows:
            item = Space(row["name"], row["address"], row["description"], row["price_per_night"], row["id"])
            spaces.append(item)
        return spaces