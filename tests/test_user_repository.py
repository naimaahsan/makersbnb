from lib.user_repository import *
import bcrypt

"""
Calling all on user repository
Gives all the users in the database
"""
def test_get_all_users(db_connection):
    db_connection.seed('seeds/makersbnb.sql')
    user_repo = UserRepository(db_connection)
    users = user_repo.all()

    assert users == [
        User('user1@email.com', '$2b$10$uQTpEo6ymYU.GLojTBG9.eH4zq4FxX5MEm5INsb7n2d4b449DapSu', 1),
        User('user2@email.com', '$2b$10$Pzf69bH7oZk3yBbeFea1HuGUcrDb9A0Q2oN1PRQicmNsFjyIDrRMS', 2),
        User('user3@email.com', '$2b$10$P0whtrX05RAam425JcGoxeAccsV1uAZGhquwiWDlXTlXpkUHmtnZy', 3)
    ]

"""
Calling create the user repository with a email and plaintext password
Adds to user to the database with a hashed password
"""
def test_create_user(db_connection):
    db_connection.seed('seeds/makersbnb.sql')
    user_repo = UserRepository(db_connection)
    result = user_repo.create('new_user@email.com', 'password123')
    assert result is None
    users = user_repo.all()
    assert len(users) == 4
    added_user = users[3]
    assert added_user.email == "new_user@email.com"
    assert bcrypt.checkpw('password123'.encode('utf-8'), added_user.password.encode('utf-8'))