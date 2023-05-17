from main import convert_value_to_centimeters, convert_value_to_kilometers, convert_value_to_meters



def test_convert_value_to_centimeters():
    value=0
    result_expected=5
    value=convert_value_to_centimeters(50)
    assert value==result_expected

def test_convert_value_to_meters():
    value=0
    result_expected=0.5
    value=convert_value_to_meters(50)
    assert value==result_expected

def test_convert_value_to_kilometers():
    value=0
    result_expected=50*0.000001
    value=convert_value_to_kilometers(50)
    assert value==result_expected
