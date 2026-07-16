from lib.space import Space, SpaceEmail
from lib.space_repository import SpaceRepository 

def test_space_repo_all_returns_all_spaces(db_connection):
    db_connection.seed("seeds/makersbnb.sql")

    repo = SpaceRepository(db_connection)

    space = repo.all()

    assert space == [
        Space('Cool House', 'Small flat', '8 Fake Street, Faketown', 100.00, 1, 1),
        Space('My House', 'Large flat', '9 Fake Street, Faketown', 125.00, 1, 2),
        Space('Top House', 'Bungalow', '15 Fake Road, Faketown', 99.00, 2, 3),
        Space('Party House', 'Penthouse', '85 Fake Road, Faketown', 200.00, 3, 4)
    ]

def test_create_new_listing(db_connection):
    db_connection.seed("seeds/makersbnb.sql")

    repo = SpaceRepository(db_connection)

    new_space = Space("Cozy Cottage", "Guest Favourite", "Cornwall", 100.00, 1)

    repo.create(new_space)

    assert repo.all() == [
        Space('Cool House', 'Small flat', '8 Fake Street, Faketown', 100.00, 1, 1),
        Space('My House', 'Large flat', '9 Fake Street, Faketown', 125.00, 1, 2),
        Space('Top House', 'Bungalow', '15 Fake Road, Faketown', 99.00, 2, 3),
        Space('Party House', 'Penthouse', '85 Fake Road, Faketown', 200.00, 3, 4),
        Space("Cozy Cottage", "Guest Favourite", "Cornwall", 100.00, 1, 5)
    ]

def test_space_repo_returns_all_with_email(db_connection):
    db_connection.seed("seeds/makersbnb.sql")

    repo = SpaceRepository(db_connection)

    space = repo.all_with_email()

    assert space == [
    SpaceEmail('Cool House', 'Small flat', '8 Fake Street, Faketown', 100.00, 'user1@email.com', 1, 1),
        SpaceEmail('My House', 'Large flat', '9 Fake Street, Faketown', 125.00, 'user1@email.com', 1, 2),
        SpaceEmail('Top House', 'Bungalow', '15 Fake Road, Faketown', 99.00, 'user2@email.com', 2, 3),
        SpaceEmail('Party House', 'Penthouse', '85 Fake Road, Faketown', 200.00, 'user3@email.com', 3, 4)
    ]