from main import balance

def test_balance():
    string = "(([]))"
    expected_result= True
    string = balance(string)
    assert string == expected_result
