from test import get_name_path_file
import os
def test_get_name_path_file():
    result = get_name_path_file("Notas.txt")
    expected_output = "The name of file is: Notas.txt\nThe path of file is: " + os.path.abspath("Notas.txt")
    assert result == expected_output
