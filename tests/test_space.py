from lib.space import Space

def test_instantiates():
    space = Space("Cozy Cottage", "Guest Favourite", "Cornwall", 100.00, 1, 1)
    assert space.id == 1 
    assert space.name == "Cozy Cottage"
    assert space.address == "Cornwall"
    assert space.description == "Guest Favourite"
    assert space.price_per_night == 100.00
    assert space.user_id == 1

def test_equality():
    space_1 = Space("Cozy Cottage", "Guest Favourite", "Cornwall", 100.00, 1, 1)
    space_2 = Space("Cozy Cottage", "Guest Favourite", "Cornwall", 100.00, 1, 1)
    assert space_1 == space_2

def test_formats_correctly():
    space = Space("Cozy Cottage", "Guest Favourite", "Cornwall", 100, 1, 1)
    assert str(space) == "Space(1, Cozy Cottage, Guest Favourite, Cornwall, 100, 1)"