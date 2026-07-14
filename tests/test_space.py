from lib.space import Space

def test_spaces_model_instances_with_name_address_description_price_per_night_id():
    # Instantiate Spaces model
    space = Space('House', '1 fake road', 'This is a nice house', 90.00, 1)
    # Assert each object attribute == provided variables
    assert space.name == 'House'
    assert space.address == '1 fake road'
    assert space.description == 'This is a nice house'
    assert space.price_per_night == 90.00
    assert space.id == 1

def test_spaces_model_formats_to_strings():
    space = Space('House', '1 fake road', 'This is a nice house', 90.00, 1)

    assert str(space) == "Space(House, 1 fake road, This is a nice house, 90.00, 1)"

def test_two_spaces_model_objects_can_be_easily_compared():
    space1 = Space('House', '1 fake road', 'This is a nice house', 90.00, 1)
    space2 = Space('House', '1 fake road', 'This is a nice house', 90.00, 1)
    assert space1 == space2
