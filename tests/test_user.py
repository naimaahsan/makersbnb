from lib.user import *

"""
A created user has all the relevant attributes
"""
def test_create_user():
    user = User("testmail@email.com", '$2b$10$uQTpEo6ymYU.GLojTBG9.eH4zq4FxX5MEm5INsb7n2d4b449DapSu', 1)
    assert user.id == 1
    assert user.email == "testmail@email.com"
    assert user.password == "$2b$10$uQTpEo6ymYU.GLojTBG9.eH4zq4FxX5MEm5INsb7n2d4b449DapSu"


"""
Two users with the same attributes
Are treated as equal
"""
def test_equal_users():
    user1 = User("testmail@email.com", '$2b$10$uQTpEo6ymYU.GLojTBG9.eH4zq4FxX5MEm5INsb7n2d4b449DapSu', 1)
    user2 = User("testmail@email.com", '$2b$10$uQTpEo6ymYU.GLojTBG9.eH4zq4FxX5MEm5INsb7n2d4b449DapSu', 1)
    assert user1 == user2

"""
Calling str on a user
Gives a nicely formatted string
"""
def test_user_str():
    user = User("testmail@email.com", '$2b$10$uQTpEo6ymYU.GLojTBG9.eH4zq4FxX5MEm5INsb7n2d4b449DapSu', 1)
    assert str(user) == "User(1, testmail@email.com, $2b$10$uQTpEo6ymYU.GLojTBG9.eH4zq4FxX5MEm5INsb7n2d4b449DapSu)"