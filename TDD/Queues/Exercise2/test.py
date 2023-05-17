from main import sort_queue

def test_sort_queue():
    values=[8, 3, 2, 1]
    expect_values=[1, 2, 3, 8]
    values= sort_queue(values)
    assert values == expect_values
