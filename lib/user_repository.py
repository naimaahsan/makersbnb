from lib.user import *
import bcrypt

class UserRepository:
    
    def __init__(self, connection):
        self._connection = connection # .connect should already have been called

    def all(self):
        user_factory = self._connection.make_class_row(User)
        return self._connection.execute(
            "SELECT * FROM users",
            row_factory = user_factory
        )

    def create(self, email, plain_password):
        salt = bcrypt.gensalt(10)
        hashed_password = bcrypt.hashpw(plain_password.encode('utf-8'), salt)
        self._connection.execute(
            "INSERT INTO users (email, password) " \
            "VALUES(%s, %s);", [email, hashed_password.decode()]
        )
        return None

    def verify_user(self, email, plain_password):
        user_factory = self._connection.make_class_row(User)
        users = self._connection.execute(
            "SELECT * FROM users " \
            "WHERE email = %s",
            [email],
            row_factory = user_factory
        )
        if len(users) != 1:
            return False
        user = users[0]
        if not bcrypt.checkpw(plain_password.encode('utf-8'), user.password.encode('utf-8')):
            return False
        return user.id
    
    def check_email_exists(self, email):
        user_factory = self._connection.make_class_row(User)
        users = self._connection.execute(
            "SELECT * FROM users " \
            "WHERE email = %s",
            [email],
            row_factory = user_factory
        )
        if len(users) != 1:
            return False
        return True