from lib.user import *

class UserRepository:
    
    def __init__(self, connection):
        self._connection = connection # .connect should already have been called

    def all(self):
        user_factory = self._connection.make_class_row(User)
        return self._connection.execute(
            "SELECT * FROM users",
            row_factory = user_factory
        )
