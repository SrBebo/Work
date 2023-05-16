from main import validate_option



def test_validate_option():
    assert validate_option('1') == True
    assert validate_option('2') == True
    assert validate_option('3') == True
    assert validate_option('4') == True
    assert validate_option('5') == True
    assert validate_option('6') == True
