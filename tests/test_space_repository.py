from lib.space import Space
from lib.space_repository import SpaceRepository

"""
Test that the all() method returns all spaces as a list of strings
"""
def test_all_method_returns_all_spaces_as_list_of_strings(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = SpaceRepository(db_connection)

    spaces = repository.all()

    assert spaces == [Space("Cool House", "8 Fake Street, Faketown", "Small flat", 100.00, 1),
    Space("My House", "9 Fake Street, Faketown", "Large flat", 125.00, 2),
    Space("Top House", "15 Fake Road, Faketown", "Bungalow", 99.00, 3),
    Space("Party House", "85 Fake Road, Faketown", "Penthouse", 200.00, 4)]