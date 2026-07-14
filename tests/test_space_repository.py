from lib.space import Space
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

    new_space = Space("Cozy Cottage", "Guest Favourite", "Cornway", 100.00, 1)

    repo.create(new_space)

    assert repo.all() == [
        Space('Cool House', 'Small flat', '8 Fake Street, Faketown', 100.00, 1, 1),
        Space('My House', 'Large flat', '9 Fake Street, Faketown', 125.00, 1, 2),
        Space('Top House', 'Bungalow', '15 Fake Road, Faketown', 99.00, 2, 3),
        Space('Party House', 'Penthouse', '85 Fake Road, Faketown', 200.00, 3, 4),
        Space("Cozy Cottage", "Guest Favourite", "Cornway", 100.00, 1, 5)
    ]
