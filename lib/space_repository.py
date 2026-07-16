from lib.space import Space, SpaceEmail

class SpaceRepository:
    def __init__(self, db_conn):
        self._connection = db_conn

    def all_with_email(self):
        query = """
            SELECT
                spaces.name,
                spaces.description,
                spaces.address,
                spaces.price_per_night,
                users.email,
                spaces.user_id,
                spaces.id,
                users.id AS host_id
            FROM spaces
            JOIN users ON spaces.user_id = users.id;
        """
        rows = self._connection.execute(query)

        spaces = []
        for row in rows:

            item = SpaceEmail(
                row["name"],
                row["description"],
                row["address"],
                row["price_per_night"],
                row["email"],
                row["user_id"],
                row["id"]
                )
            spaces.append(item)

        return spaces

    def all(self):
        rows = self._connection.execute("SELECT * FROM spaces;")

        spaces = []
        for row in rows:

            item = Space(
                row["name"],
                row["description"],
                row["address"],
                row["price_per_night"],
                row["user_id"],
                row["id"]
                )
            spaces.append(item)

        return spaces
    
        
    def create(self, space):
        self._connection.execute(
            'INSERT INTO spaces (name, description, address, price_per_night, user_id) VALUES (%s, %s, %s, %s, %s)', 
            [space.name, space.description, space.address, space.price_per_night, space.user_id])
        
        return None
    
    def find(self, id):
        row = self._connection.execute("""SELECT
                spaces.name,
                spaces.description,
                spaces.address,
                spaces.price_per_night,
                users.email,
                spaces.user_id,
                spaces.id,
                users.id AS host_id
            FROM spaces
            JOIN users ON spaces.user_id = users.id
            WHERE spaces.id = %s;""", [id])[0]

        space = SpaceEmail(
                row["name"],
                row["description"],
                row["address"],
                row["price_per_night"],
                row["email"],
                row["user_id"],
                row["id"]
                )
        return space